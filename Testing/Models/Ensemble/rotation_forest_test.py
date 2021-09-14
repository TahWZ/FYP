import sys
import unittest
sys.path.append("../../../Program/Algorithm/pred_mdls/ensemble") #Adds directory containing jupyter import and module to test
from Rotation_Forest import rotation_forest_model
#========== For tests setup ==========
import warnings
from rotation_forest import RotationForestClassifier as RFC
from scipy.io import arff
import pandas as pd
import numpy as np

class Rotation_forest_test(unittest.TestCase):
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
        rf1 = RFC()
        rf2 = rotation_forest_model(self.data1)
        self.assertTrue(type(rf1) == type(rf2))

    def test2(self):
        #Test case ID: 2
        rf = rotation_forest_model(self.data1)
        pred_test = [[0,1,0,1,0,1]] #Appropriate size
        try:
            res = rf.predict(pred_test)
            self.assertEqual(len(res),1)
        except:
            assert False, "Test failed, prediction unsuccessful with valid test data"

    def test3(self):
        #Test case ID: 3
        rf = rotation_forest_model(self.data1)
        pred_test = [[0,1,0]] #Invalid size
        try:
            rf.predict(pred_test)
            assert False, "Test failed, prediction successful with invalid test data"
        except:
            pass

    def test4(self):
        #Test case ID: 4
        rf = rotation_forest_model(self.data1)
        pred_test = [[0,1,0,1,0,1]]*27 #Appropriate size
        try:
            res = rf.predict(pred_test)
            self.assertEqual(len(res),27)
        except:
            assert False, "Test failed, prediction unsuccessful with valid test data"

    def test5(self):
        #Test case ID: 5
        try:
            with warnings.catch_warnings():
                warnings.simplefilter('ignore', category=RuntimeWarning)
                rf = rotation_forest_model(self.data2)
                test_predict = self.data2[0][4:6]
                res = rf.predict(test_predict)
                self.assertEqual(len(res),2)
        except:
            assert False, "Test failed, prediction unsuccessful for actual dataset"



#====================( Main )====================
if __name__=='__main__':
    unittest.main()
