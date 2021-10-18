import csv
import numpy as np
import pandas as pd
from scipy.io import arff
import math
import warnings # Suppress Warnings
warnings.filterwarnings('ignore')
#Import data preprocessing techniques
from data_preproc.Preprocess import preprocess, Normalize
#Import models
from pred_mdls.base.Complement_Naive_Bayes import complement_naive_bayes_model
from pred_mdls.base.Decision_Tree import decision_tree_model
from pred_mdls.base.Logistic_Regression import logistic_regression_model
from pred_mdls.base.Multi_Layer_Perceptron import multi_layer_perceptron_model
from pred_mdls.base.Naive_Bayes import naive_bayes_model
from pred_mdls.ensemble.Random_Forest import random_forest_model
from pred_mdls.ensemble.Rotation_Forest import rotation_forest_model
from pred_mdls.ensemble.Voting import voting_model
#Import feature selection techniques
from data_preproc.fs_tech.CFS import cfs_algo
from data_preproc.fs_tech.RFE import rfe_algo
#Import model evaluation methods
from pf_eval.Confusion_Matrix import confusion_matrix_model
from pf_eval.AUC_ROC import auc_roc_model
from pf_eval.F1_Score import f1_model

def data_conversion(data):
    """
    Converts the string labels in arff files to appropriate integer values
    """
    for i in range(len(data)): #For each row in the dataset
        if data[i] == b'N' or data[i] == b'false' or data[i] == b'no':
            data[i] = 0
        else:
            data[i] = 1
    return data

def read_data(filename):
    """
    Read the data from arff files, then converting the array into a
    Pandas Dataframe
    """
    data = arff.loadarff(filename)
    loaddata = pd.DataFrame(data[0])
    return loaddata

def evaluate_data(model,X_test,y_test):
    """
    Evaluates a given model using evulations functions which returns
    the score of the following evaluation metrics:
    1. AUC
    2. F1-Score
    3. False Positive Rate
    4. False Negative Rate
    """
    auc_score = auc_roc_model(model,X_test,y_test)
    f1_score = f1_model(model,X_test,y_test)
    fpr,fnr = confusion_matrix_model(model,X_test,y_test)
    return auc_score,f1_score,fpr,fnr
    
def csv_writer(datasets, savename, results, model_name, pp_name):
    """
    Creates/Modify csv file which contains the results of the program
    """
    header = ['Model name'] + model_name
    n = len(model_name)
    with open('csv_results/' + savename + '.csv','w',encoding='UTF8', newline='') as csv_file:
        res = csv.writer(csv_file)
        for k in range(len(results[0])):
            # Adds label, indicating result type (AUC, F1, FPR, FNR)
            res.writerow([results[0][k][0]])
            # Adds legend, containing the model names
            res.writerow(header)
            # For each dataset
            for j in range(len(results)):
                col_num = 0
                # For each model
                for i in range(len(pp_name[j])): 
                    # Add performance result of model for the current dataset
                    res.writerow([f'{datasets[j]} ({pp_name[j][i]})'] + results[j][k][1][col_num:col_num+n])
                    col_num += n
            # Adds row skip between result types
            if k != len(results[0])-1:
                res.writerow('')

def feature_selection(fs_res,loaddata,data,train_size,k_fold):
    """
    Performs the required feature selection methods based on the first parameter
    """
    # The result array
    pp_arr = []
    # The feature selection methods (CFS, RFE)
    feature_funcs = [cfs_algo,rfe_algo]
    # Check if the dataset with all its metrics is required
    if fs_res[0]:
        try:
            # Adds the preprocessed dataset, with no feature selection method performed
            pp_arr.append(preprocess(loaddata,k_fold))
        except:
            return False, 1
    # Checks which feature selection methods to perform
    for i in range(1,len(fs_res)):
        if fs_res[i]:
            # Performs the required feature selection
            try: # Error handling (Invalid train size)
                _,f_selection = feature_funcs[i-1](data,train_size)
            except:
                return False, 2
            # Preprocesses the dataset
            try: # Error handling (Reduced dataset not suited for k-fold value set)
                pp_arr.append(preprocess(loaddata,k_fold,f_selection))
            except:
                return False, 1
    return pp_arr

def model_creation(base_preds,ensemble_preds,data):
    """
    Builds the required prediction models using training data provided.
    Models built are based on the user selections.
    """
    models = []
    # Hyperparameter for the tree models
    args = [108]
    # The base prediction models
    base_funcs = [
        complement_naive_bayes_model,
        decision_tree_model,
        logistic_regression_model,
        multi_layer_perceptron_model,
        naive_bayes_model 
    ]
    # The ensemble prediction models
    ensemble_funcs = [
        random_forest_model,
        rotation_forest_model,
        voting_model
    ]
    # Checks the user selections and builds the required base models
    for index in base_preds:
        models.append(base_funcs[index](data))
    # Checks the user selections and builds the required ensemble models
    for index in ensemble_preds:
        models.append(ensemble_funcs[index](data,args))
    return models

def main_algo_run(filename,fs_res,pred_res,train_res):
    """
    Main algorithm, utilizes various functions within the system to performs the following processes(ordered):
    1. Retrieve the user selections for prediction models, training settings and feature selection methods
    2. Perform required feature selection and preprocesses
    3. Builds required prediction models
    4. Evaluate performance of models
    5. Return results
    """
    try:
        loaddata = read_data(filename)
        loaddata = Normalize(loaddata)
    except:
        return False, 0
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
    if len(pp_arr) == 2 and pp_arr[0] == False:
        return pp_arr[0], pp_arr[1]
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
    folds = k_fold
    for j,pp in enumerate(pp_arr): #For each preprocessed dataset
        for i in range(folds):
            data = [pp[i][0],pp[i][2]]
            models = model_creation(base_preds,ensemble_preds,data)
            for k in range(len(models)): #For every model selected
                auc_score,f1_score,fpr,fnr = evaluate_data(models[k],pp[i][1],pp[i][3])
                if math.isnan(auc_score):
                    auc_score = 0
                auc_arr[(j*len(model_name))+k] += auc_score
                f1_arr[(j*len(model_name))+k] += f1_score
                fpr_arr[(j*len(model_name))+k] += fpr
                fnr_arr[(j*len(model_name))+k] += fnr

    for i in range(len(auc_arr)): #Retrieves the average scores between each folds
        auc_arr[i] /= folds
        auc_arr[i] = round(auc_arr[i],3)
        f1_arr[i] /= folds
        f1_arr[i] = round(f1_arr[i],3)
        fpr_arr[i] /= folds
        fpr_arr[i] = round(fpr_arr[i],3)
        fnr_arr[i] /= folds
        fnr_arr[i] = round(fnr_arr[i],3)
    header.append('Model Name')
    for i in model_name: #Apped header with models used
        header.append(i[0]) 
    result.append(('AUC', auc_arr))
    result.append(('F1 Score', f1_arr))
    result.append(('False Positive Rate', fpr_arr))
    result.append(('False Negative Rate', fnr_arr))
    return model_name,pp_name,result

