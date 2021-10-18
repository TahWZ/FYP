#==== Imports ====#
# !pip install rotation-forest
from sklearn import metrics
from rotation_forest import RotationForestClassifier as RFC
from scipy.io import arff
from sklearn.model_selection import train_test_split as ts
import pandas as pd
import numpy as np
#=================#

#==== Functions ====#
def rotation_forest_model(data, args=None):
    """
    Rotation forest ensemble model
    """
    forest = RFC()
    forest.fit(data[0],data[1])
    return forest
#===================#