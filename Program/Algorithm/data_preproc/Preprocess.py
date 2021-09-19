from collections import Counter
from scipy.io import arff
from sklearn.model_selection import train_test_split as ts
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from imblearn.under_sampling import InstanceHardnessThreshold
import numpy as np
import pandas as pd

def Normalize(data):
    i_size = len(data) #The initial size of the data
    #Remove missing values
    r_data = data.dropna()
    r_size = len(r_data) #The data size after removing missing values
    if r_size/i_size > 0.8: #To ensure no false data removal was performed
        data = r_data
    #Remove outliers
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    result = data[~((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)]
    return result

def K_fold(data,f=5):
    kf = KFold(n_splits=f)
    tt_splits = kf.split(data)
    return tt_splits

def Stratifid_K_fold(X,y,f=5):
    skf = StratifiedKFold(n_splits=f)
    tt_splits = skf.split(X,y)
    return tt_splits

def IHT(data,k_fold):   
    gauss_iht = InstanceHardnessThreshold(cv=k_fold)
    underX, underY = gauss_iht.fit_resample(data[0],data[1])
    return underX, underY

def data_conversion(data):
    for i in range(len(data)):
        if data[i] == b'N' or data[i] == b'false' or data[i] == b'no':
            data[i] = 0
        else:
            data[i] = 1
    return data

def preprocess(data, k_fold, fs = []):
    SM = np.array(data.iloc[:,:-1]) #Software metrics
    if len(fs) != 0:
        SM = SM[:,fs]
    L = data_conversion(np.array(data.iloc[:,-1])).astype(int) #Labels
    tt_splits = Stratifid_K_fold(SM,L,k_fold)
    # classes = {
    #     '0':0,
    #     '1':0 
    # }
    # percentage = {
    #     '0':f'0%',
    #     '1':f'0%'
    # }
    # for c in L:
    #     classes[str(c)] += 1
    #     percentage[str(c)] = f'{round((classes[str(c)]/len(L))*100,2)}%'
    # print(f'Classes: {classes}')
    # print(f'Percentage: {percentage}')
    #IHT
    result = []
    for train, test in tt_splits:
        # print(f'Train: {train} Train Shape: {train.shape}')
        # print(f'Test: {test} Test Shape: {test.shape}\n')
        # print(f'SM[train]: {SM[train]}')
        # print(f'L[train]: {L[train]}')
        SM_under, L_under = IHT([SM[train],L[train]],k_fold)
        result.append([SM_under, SM[test], L_under, L[test]])
    return result
