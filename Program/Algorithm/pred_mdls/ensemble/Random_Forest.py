#==== Imports ====#
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from scipy.io import arff
from sklearn.model_selection import train_test_split as ts
import pandas as pd
import numpy as np
#=================#

#==== Functions ====#
def random_forest_model(data, args=[1000]):
    '''
    Arguments:
    1. Data
    2. List of arguments for model (Number of Estimators)
    
    Output:
    2. Model
    '''
    rf = RandomForestClassifier(n_estimators = args[0])
    rf.fit(data[0], data[1])
    return rf
#===================#