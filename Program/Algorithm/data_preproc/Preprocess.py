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

def IHT(data):   
    gauss_iht = InstanceHardnessThreshold()
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
    if fs != []:
        SM = SM[:,fs]
    L = data_conversion(np.array(data.iloc[:,-1])).astype(int) #Labels
    tt_splits = Stratifid_K_fold(SM,L,k_fold)
    #IHT
    result = []
    for train, test in tt_splits:
        SM_under, L_under = IHT([SM[train],L[train]])
        result.append([SM_under, SM[test], L_under, L[test]])
    return result
