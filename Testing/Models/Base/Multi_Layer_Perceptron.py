#==== Imports ====#
import unittest
import numpy as np
import pandas as pd
from scipy.io import arff
from sklearn.model_selection import train_test_split as ts
from sklearn import metrics
from sklearn.neural_network import MLPClassifier
#=================#

#==== Functions ====#
def multi_layer_perceptron_model(data,args=None):
    mlp = MLPClassifier(solver='lbfgs',max_iter=10000000000)
    mlp.fit(data[0],data[1])
    return mlp

def dummy_data(filename = 'CM1.arff.txt' ):
    #File
    data = arff.loadarff(filename)
    loaddata = pd.DataFrame(data[0])

    #Software metrics and decisions
    SM = np.array(loaddata[['LOC_BLANK','BRANCH_COUNT','CALL_PAIRS','LOC_CODE_AND_COMMENT']]) #Software metrics
    L = np.array(loaddata['Defective']) #label
    SM2 = np.array(loaddata[['LOC_BLANK','BRANCH_COUNT','CALL_PAIRS']])
    SM_train, SM_test, L_train, L_test = ts(SM,L,test_size = 0.1)
    SM2_train, SM2_test, L2_train, L2_test = ts(SM2,L,test_size = 0.1)
    L_train=L_train.astype('str')
    L_test=L_test.astype('str')
    return [SM_train,L_train], SM2_test, SM_test,L_test
#===================#

class mlp_test(unittest.TestCase):

    def test_type(self):
        dummy = dummy_data()
        mlp = multi_layer_perceptron_model(dummy[0])
        mlp2 = MLPClassifier(solver='lbfgs',max_iter=10000000000)
        self.assertTrue(type(mlp) == type(mlp2))
    
    def test_empty(self):
        try:
            mlp = multi_layer_perceptron_model([])
        except IndexError:
            fail = True
        self.assertTrue(fail)
    
    def test_fit(self):
        dummy = dummy_data()
        lr = multi_layer_perceptron_model(dummy[0])
        try:
            lr.predict(dummy[1])
        except ValueError:
            fail = True
        self.assertTrue(fail)
    
    def test_normal(self):
        dummy = dummy_data()
        mlp = multi_layer_perceptron_model(dummy[0])
        prediction = mlp.predict(dummy[2])
        res = metrics.accuracy_score(dummy[3], prediction)
        self.assertTrue(res >= 0.75)

#====================( Main )====================
if __name__=='__main__':
    unittest.main()
