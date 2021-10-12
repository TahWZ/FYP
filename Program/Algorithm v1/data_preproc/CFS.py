#==== Imports ====#
from scipy.io import arff
import numpy as np
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
#=================#

#==== Functions ====#
def cfs_algo(data, n_k=10):
    cfs = SelectKBest(score_func=f_classif, k=n_k)
    cfs.fit(data[0],data[1])
    supports = cfs.get_support(True)
    selections = []
    for i in range(len(data[0][0])):
        if i in supports:
            selections.append(True)
        else:
            selections.append(False)
    return cfs, selections

def data_conversion(data):
    for i in range(len(data)):
        if data[i] == b'N':
            data[i] = 0
        else:
            data[i] = 1
    return data
#===================#
