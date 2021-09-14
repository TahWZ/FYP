import numpy as np
import pandas as pd
from scipy.io import arff
from matplotlib import pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score

def auc_roc_model(model,X_test,y_test):
    model_probs = model.predict_proba(X_test)
    model_probs = model_probs[:, 1]
    auc_score = roc_auc_score(y_test,model_probs)
    return auc_score
