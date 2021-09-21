#==== Imports ====#
from imblearn.under_sampling import InstanceHardnessThreshold

#==== Functions ====#
def iht(data, k_fold):   
    while k_fold >= 2:
        try:
            gauss_iht = InstanceHardnessThreshold(cv=k_fold)
            underX, underY = gauss_iht.fit_resample(data[0],data[1])
            return underX, underY
        except:
            k_fold -= 1
    return data[0],data[1]

def data_conversion(data_column):
    for i in range(len(data_column)):
        if data_column[i] == b'N':
            data_column[i] = 0
        else:
            data_column[i] = 1
    return data_column
