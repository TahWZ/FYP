import sys
import unittest
sys.path.append("../../../Program/Algorithm/pred_mdls/ensemble") #Adds directory containing jupyter import and module to test
from Random_Forest import random_forest_model
#========== For tests setup ==========
from sklearn.ensemble import RandomForestClassifier
from scipy.io import arff
import pandas as pd
import numpy as np

class Random_forest_test(unittest.TestCase):
    def setUp(self):
        def data_conversion(data):
            for i in range(len(data)):
                if data[i] == b'N' or data[i] == b'false' or data[i] == b'no':
                    data[i] = 0
                else:
                    data[i] = 1
            return data
        data = arff.loadarff("test1.arff.txt")
        loaddata1 = pd.DataFrame(data[0])
        #Extracted from function
        SM = np.array(loaddata1.iloc[:,:-1]) 
        L = data_conversion(np.array(loaddata1.iloc[:,-1])).astype(int)
        self.data1 = [SM, L]
        data = arff.loadarff("test2.arff.txt")
        loaddata2 = pd.DataFrame(data[0])
        #Extracted from function
        SM = np.array(loaddata2.iloc[:,:-1]) 
        L = data_conversion(np.array(loaddata2.iloc[:,-1])).astype(int)
        self.data2 = [SM, L]

    def test1(self):
        #Test case ID: 1
        rf1 = RandomForestClassifier(n_estimators = 100)
        rf2 = random_forest_model(self.data1)
        self.assertTrue(type(rf1) == type(rf2))

    def test2(self):
        #Test case ID: 2
        rf = random_forest_model(self.data1)
        pred_test = [[0,1,0,1,0,1]] #Appropriate size
        try:
            res = rf.predict(pred_test)
            self.assertEqual(len(res),1)
        except:
            assert False, "Test failed, prediction unsuccessful with valid test data"

    def test3(self):
        #Test case ID: 3
        rf = random_forest_model(self.data1)
        pred_test = [[0,1,0]] #Invalid size
        try:
            rf.predict(pred_test)
            assert False, "Test failed, prediction successful with invalid test data"
        except:
            pass

    def test4(self):
        #Test case ID: 4
        rf = random_forest_model(self.data1)
        self.assertTrue(rf.get_params()["n_estimators"]==108)

    def test5(self):
        #Test case ID: 5
        rf = random_forest_model(self.data1, args = [64])
        self.assertTrue(rf.get_params()["n_estimators"]==64)

    def test6(self):
        #Test case ID: 6
        rf = random_forest_model(self.data1)
        pred_test = [[0,1,0,1,0,1]]*27 #Appropriate size
        try:
            res = rf.predict(pred_test)
            self.assertEqual(len(res),27)
        except:
            assert False, "Test failed, prediction unsuccessful with valid test data"

    def test7(self):
        #Test case ID: 7
        rf = random_forest_model(self.data2)
        test_predict = self.data2[0][1:3]
        try:
            res = rf.predict(test_predict)
            self.assertEqual(len(res),2)
        except:
            assert False, "Test failed, prediction unsuccessful for actual dataset"



#====================( Main )====================
if __name__=='__main__':
    unittest.main()
