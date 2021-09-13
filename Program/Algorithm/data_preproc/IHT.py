#==== Imports ====#
from imblearn.under_sampling import InstanceHardnessThreshold

#==== Functions ====#
def iht(data):   
    under_iht = InstanceHardnessThreshold()
    underX, underY = under_iht.fit_resample(data[0],data[1])
    return underX, underY

def data_conversion(data_column):
    for i in range(len(data_column)):
        if data_column[i] == b'N':
            data_column[i] = 0
        else:
            data_column[i] = 1
    return data_column
