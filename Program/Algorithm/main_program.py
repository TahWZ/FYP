import csv
import sys
import numpy as np
import pandas as pd
from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn import metrics
import math
#import jupyter_import # Allows jupyter notebook to be imported
import warnings # Suppress Warnings
warnings.filterwarnings('ignore')
from data_preproc.Preprocess import preprocess, Normalize
from pred_mdls.base.Complement_Naive_Bayes import complement_naive_bayes_model
from pred_mdls.base.Decision_Tree import decision_tree_model
from pred_mdls.base.Logistic_Regression import logistic_regression_model
from pred_mdls.base.Multi_Layer_Perceptron import multi_layer_perceptron_model
from pred_mdls.base.Naive_Bayes import naive_bayes_model
from pred_mdls.ensemble.Random_Forest import random_forest_model
from pred_mdls.ensemble.Rotation_Forest import rotation_forest_model
from pred_mdls.ensemble.Voting import voting_model
from pf_eval.AUC_ROC import auc_roc_model
from pf_eval.F1_Score import f1_model
from pf_eval.CSV import write_results
from data_preproc.CFS import cfs_algo
from data_preproc.RFE import rfe_algo
from data_preproc.RR import ridge_algo
from pf_eval.Confusion_Matrix import confusion_matrix_model

def data_conversion(data):
    for i in range(len(data)):
        if data[i] == b'N' or data[i] == b'false' or data[i] == b'no':
            data[i] = 0
        else:
            data[i] = 1
    return data

def read_data(filename):
    data = arff.loadarff(filename)
    loaddata = pd.DataFrame(data[0])
    return loaddata

def process_data(loaddata,features):
    # Features are selected based on CFS
    software_metrics = np.array(loaddata[features])
    labels = np.array(loaddata['Defective'])
    return software_metrics,labels

def train_data(software_metrics,labels):
    X_train, X_test, y_train, y_test = train_test_split(software_metrics, labels, test_size = 0.1)
    y_train = y_train.astype('str')
    y_test = y_test.astype('str')
    return X_train, X_test, y_train, y_test

def evaluate_data(model,X_test,y_test):
    auc_score = auc_roc_model(model,X_test,y_test)
    f1_score = f1_model(model,X_test,y_test)
    fpr,fnr = confusion_matrix_model(model,X_test,y_test)
    return auc_score,f1_score,fpr,fnr

def translate(result):
    count = 1
    res = []
    while count <= 3:
        for i in range(len(result[0])):
            res.append([result[0][i], result[1][((i+1)*count)-1],result[2][((i+1)*count)-1]])
        count += 1
    return res

def main_writer(header,result):
    #Writes the output of a single dataset for main function
    filters = ['No filter','CFS','RFE']
    with open('pred_results.csv','w',encoding='UTF8', newline='') as file:
        res = csv.writer(file)
        for i in range(len(filters)):
            res.writerow('')
            res.writerow([filters[i]])
            res.writerow(header)
            res.writerow([result[0][0]] + result[0][1][i*8:i*8+8])
            res.writerow([result[1][0]] + result[1][1][i*8:i*8+8])
    
def run(datasets, savename, results, model_name, pp_name):
    #Writes the output of multiple datasets for the main function
    header = ['Model name'] + model_name
    n = len(model_name)
    with open('csv_results/' + savename + '.csv','w',encoding='UTF8', newline='') as csv_file:
        res = csv.writer(csv_file)
        for k in range(len(results[0])):
            # AUC, F1, FPR, FNR
            res.writerow([results[0][k][0]])
            # Model Name
            res.writerow(header)
            for j in range(len(results)):
                col_num = 0
                for i in range(len(pp_name[j])):
                    res.writerow([f'{datasets[j]} ({pp_name[j][i]})'] + results[j][k][1][col_num:col_num+n])
                    col_num += n
            if k != len(results[0])-1:
                res.writerow('')

def feature_selection(fs_res,loaddata,data,train_size,k_fold):
    pp_arr = []
    feature_funcs = [cfs_algo,rfe_algo]
    if fs_res[0]:
        pp_arr.append(preprocess(loaddata,k_fold))
    for i in range(1,len(fs_res)):
        if fs_res[i]:
            _,f_selection = feature_funcs[i-1](data,train_size)
            pp_arr.append(preprocess(loaddata,k_fold,f_selection))
    return pp_arr

def model_creation(base_preds,ensemble_preds,data):
    models = []
    args = [108]
    base_funcs = [
        complement_naive_bayes_model,
        decision_tree_model,
        logistic_regression_model,
        multi_layer_perceptron_model,
        naive_bayes_model 
    ]
    ensemble_funcs = [
        random_forest_model,
        rotation_forest_model,
        voting_model
    ]
    for index in base_preds:
        models.append(base_funcs[index](data))
    for index in ensemble_preds:
        models.append(ensemble_funcs[index](data,args))
    return models

def main_algo_run(filename,fs_res,pred_res,train_res):
    # Read the file
    loaddata = read_data(filename)
    loaddata = Normalize(loaddata)
    SM = np.array(loaddata.iloc[:,:-1]) #Software metrics
    L = data_conversion(np.array(loaddata.iloc[:,-1])).astype(int) #Labels
    data = [SM,L]
    lookup_model = ['Complement Naive Bayes','Decision Tree','Logistic regression','Multi Layer Perceptron','Naive Bayes',
            'Random Forest','Rotation Forest','Voting'] #Models used
    lookup_pp = ['All','CFS','RFE']
    fs_arr = [i for i in range(len(fs_res)) if fs_res[i]]
    pp_name = [lookup_pp[i] for i in fs_arr]
    train_size = int(train_res['tt']) if not train_res['tt'] == '' else 10
    k_fold = int(train_res['kfold']) if not train_res['kfold'] == '' else 5
    pp_arr = feature_selection(fs_res,loaddata,data,train_size,k_fold)
    base_preds = [i for i,pred in enumerate(pred_res['base']) if pred == 1]
    ensemble_preds = [i for i,pred in enumerate(pred_res['ensemble']) if pred == 1]
    model_name = [lookup_model[index] for index in base_preds] + [lookup_model[index+5] for index in ensemble_preds]
    length_preds = len(base_preds) + len(ensemble_preds)
    result = []
    arr_size = length_preds*len(pp_name) #Result array size
    auc_arr = [0]*arr_size
    f1_arr = [0]*arr_size
    fpr_arr = [0]*arr_size
    fnr_arr = [0]*arr_size
    header = []
    folds = 5
    for j,pp in enumerate(pp_arr):
        for i in range(folds):
            data = [pp[i][0],pp[i][2]]
            models = model_creation(base_preds,ensemble_preds,data)
            for k in range(len(models)):
                auc_score,f1_score,fpr,fnr = evaluate_data(models[k],pp[i][1],pp[i][3])
                if math.isnan(auc_score):
                    #print(model_name[k], auc_score)
                    auc_score = 0
                auc_arr[(j*len(model_name))+k] += auc_score
                f1_arr[(j*len(model_name))+k] += f1_score
                fpr_arr[(j*len(model_name))+k] += fpr
                fnr_arr[(j*len(model_name))+k] += fnr

    for i in range(len(auc_arr)):
        auc_arr[i] /= folds
        auc_arr[i] = round(auc_arr[i],3)
        f1_arr[i] /= folds
        f1_arr[i] = round(f1_arr[i],3)
        fpr_arr[i] /= folds
        fpr_arr[i] = round(fpr_arr[i],3)
        fnr_arr[i] /= folds
        fnr_arr[i] = round(fnr_arr[i],3)
    header.append('Model Name')
    for i in model_name:
        header.append(i[0]) 
    result.append(('AUC', auc_arr))
    result.append(('F1 Score', f1_arr))
    result.append(('False Positive Rate', fpr_arr))
    result.append(('False Negative Rate', fnr_arr))
    return model_name,pp_name,result
      
if __name__=='__main__':
    N_filenames = ['CM1.arff','JM1.arff','KC1.arff','KC3.arff',
                   'KC4.arff','MC1.arff','MC2.arff','MW1.arff',
                   'PC1.arff','PC2.arff','PC3.arff','PC4.arff','PC5.arff']
    P_filenames = ['cm1.arff','jm1.arff','kc1.arff','kc2.arff','pc1.arff']
    #run(N_filenames,'NASA.csv','NASA')
    #run(P_filenames,'PROMISE.csv','PROMISE')
    #========== Running main program =========#
    result, header = main_algo_run('datasets/NASA/CM1.arff.txt')
    main_writer(header,result)
