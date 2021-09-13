#==== Imports ====#
import numpy as np
import pandas as pd
from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
#=================#

#==== Functions ====#
def decision_tree_model(data,args=None):
    dt = DecisionTreeClassifier()
    dt.fit(data[0],data[1])
    return dt
#===================#