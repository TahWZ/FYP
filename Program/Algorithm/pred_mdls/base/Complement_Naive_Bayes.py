from sklearn.naive_bayes import ComplementNB as cnb
from scipy.io import arff
from sklearn.model_selection import train_test_split as ts
import pandas as pd
import numpy as np

def complement_naive_bayes_model(data, args=None):
    CBayes = cnb()
    CBayes.fit(data[0],data[1])
    return CBayes