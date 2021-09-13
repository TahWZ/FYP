import numpy as np
import pandas as pd
from scipy.io import arff
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score

def f1_model(model,X_test,y_test):
    y_pred = model.predict(X_test)
    result = f1_score(y_test,y_pred,pos_label=1,zero_division=0)
    return result