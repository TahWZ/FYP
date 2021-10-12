# import numpy as np
# import pandas as pd
# from scipy.io import arff
from sklearn.metrics import confusion_matrix

def confusion_matrix_model(model,X_test,y_test):
    y_pred = model.predict(X_test)
    tn,fp,fn,tp = confusion_matrix(y_test, y_pred).ravel()
    if (tn+fp) == 0:
        FPR = 0
    else:
        FPR = round(fp/(tn+fp),2)
    if (fn+tp) == 0:
        FNR = 0
    else:
        FNR = round(fn/(fn+tp),2)
    return FPR,FNR