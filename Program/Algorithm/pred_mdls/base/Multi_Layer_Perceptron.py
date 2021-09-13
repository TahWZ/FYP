#==== Imports ====#
import numpy as np
import pandas as pd
from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.neural_network import MLPClassifier
#=================#

#==== Functions ====#
def multi_layer_perceptron_model(data,args=None):
    mlp = MLPClassifier(solver='lbfgs',max_iter=10000000000)
    mlp.fit(data[0],data[1])
    return mlp
#===================#