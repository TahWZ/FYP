#==== Imports ====#
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split as ts
from scipy.io import arff
import pandas as pd
import numpy as np
#=================#

#==== Functions ====#
def ridge_algo(data):
    ridge = Ridge(alpha=1.0)
    ridge.fit(data[0],data[1])
    return ridge

def data_conversion(data_column):
    for i in range(len(data_column)):
        if data_column[i] == b'N':
            data_column[i] = 0
        else:
            data_column[i] = 1
    return data_column
#===================#
