import unittest
from sklearn.naive_bayes import ComplementNB as CNB
from scipy.io import arff
from sklearn.model_selection import train_test_split as ts
import pandas as pd
import numpy as np
from sklearn import metrics

def complement_naive_bayes_model(data, args=None):
    CBayes = CNB()
    CBayes.fit(data[0],data[1])
    return CBayes

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

class cnb_test(unittest.TestCase):

    def test_type(self):
        dummy = dummy_data()
        cnb = complement_naive_bayes_model(dummy[0])
        cnb2 = CNB()
        self.assertTrue(type(cnb) == type(cnb2))
    
    def test_empty(self):
        try:
            cnb = complement_naive_bayes_model([])
        except IndexError:
            fail = True
        self.assertTrue(fail)
    
    def test_fit(self):
        dummy = dummy_data()
        lr = complement_naive_bayes_model(dummy[0])
        try:
            lr.predict(dummy[1])
        except ValueError:
            fail = True
        self.assertTrue(fail)
    
    def test_normal(self):
        dummy = dummy_data()
        cnb = complement_naive_bayes_model(dummy[0])
        prediction = cnb.predict(dummy[2])
        res = metrics.accuracy_score(dummy[3], prediction)
        print(res)
        self.assertTrue(res >= 0.35)

#====================( Main )====================
if __name__=='__main__':
    unittest.main()