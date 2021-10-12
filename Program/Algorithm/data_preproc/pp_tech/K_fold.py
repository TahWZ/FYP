#==== Imports ====
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold

#==== Functions ====
def K_fold(data,f=10,read=True):
    kf = KFold(n_splits=f)
    tt_splits = kf.split(data)
    if read:
        for train_index, test_index in kf.split(data):
            print('Training data index:', train_index, '\nTest data index:', test_index, '\n')
    return tt_splits

def Stratified_K_fold(X,y,f=5):
    skf = StratifiedKFold(n_splits=f)
    tt_splits = skf.split(X,y)
    return tt_splits