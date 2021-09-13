#==== Imports ====#
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB as Gauss
from scipy.io import arff
from sklearn.model_selection import train_test_split as ts
import pandas as pd
import numpy as np
#=================#

#==== Functions ====#
def naive_bayes_model(data, args=None):
    bayes = Gauss()
    bayes.fit(data[0],data[1])
    return bayes
#===================#