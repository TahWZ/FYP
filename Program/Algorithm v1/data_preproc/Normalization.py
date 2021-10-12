#==== Imports ====#
import numpy as np
import pandas as pd
from scipy.io import arff
#=================#

#==== Functions ====#
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
#===================#
