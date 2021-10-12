#==== Imports ====#
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split as ts
from scipy.io import arff
import pandas as pd
import numpy as np
#=================#

#==== Functions ====#
def data_conversion(data_column):
    for i in range(len(data_column)):
        if data_column[i] == b'N':
            data_column[i] = 0
        else:
            data_column[i] = 1
    return data_column

def rfe_algo(data, n_k=10):
    model = LogisticRegression(max_iter=10000000000) 
    model = RFE(model, n_features_to_select=n_k)
    rfe = model.fit(data[0], data[1])
    selections = rfe.support_
    return rfe, selections
#===================#
