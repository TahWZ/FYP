#==== Imports ====
from sklearn.model_selection import KFold

#==== Functions ====
def K_fold(data,f=10,read=True):
    kf = KFold(n_splits=f)
    tt_splits = kf.split(data)
    if read:
        for train_index, test_index in kf.split(data):
            print('Training data index:', train_index, '\nTest data index:', test_index, '\n')
    return tt_splits
