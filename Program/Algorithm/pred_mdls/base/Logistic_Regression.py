#==== Imports ====#
import numpy as np
import pandas as pd
from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
#=================#

#==== Functions ====#
def logistic_regression_model(data,args=None):
    lr = LogisticRegression(solver='lbfgs',max_iter=10000000000)
    lr.fit(data[0],data[1])
    return lr
#===================#