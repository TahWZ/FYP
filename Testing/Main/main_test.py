import sys
import unittest
sys.path.append("../../Program/Algorithm") #Adds directory containing jupyter import and module to test

from main_program import read_data, process_data, data_conversion, evaluate_data, run, feature_selection, model_creation, main_algo_run
#========== For tests setup ==========
from scipy.io import arff
import pandas as pd
import numpy as np

class main_test_1(unittest.TestCase):
    #Test suite 1

    def test1(self):
        '''
        Test suite: 1
        Test case ID: 1
        '''
        output = read_data("test1.arff.txt")
        #Expected results
        exp_columns = ['metric1', 'metric2', 'metric3', 'metric4', 'label']
        exp_values = [[0.0, 0.0, 0.0, 0.0, b'N'],
                        [0.0, 0.0, 0.0, 1.0, b'Y'],
                        [0.0, 0.0, 1.0, 1.0, b'N'],
                        [0.0, 1.0, 1.0, 1.0, b'Y'],
                        [1.0, 1.0, 1.0, 1.0, b'N']]
        self.assertEqual(output.columns.tolist(), exp_columns)
        self.assertEqual(output.values.tolist(), exp_values)

    def test2(self):
        '''
        Test suite: 1
        Test case ID: 2
        '''
        loaddata = read_data("test1.arff.txt")
        #Extracted from function
        SM = np.array(loaddata.iloc[:,:-1]) #Software metrics
        L = np.array(loaddata.iloc[:,-1])
        exp_values = [[0.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0],
                    [0.0, 0.0, 1.0, 1.0],
                    [0.0, 1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0, 1.0]]
        exp_labels = [b'N',b'Y',b'N',b'Y',b'N']
        self.assertEqual(SM.tolist(), exp_values)
        self.assertEqual(L.tolist(), exp_labels)

    def test3(self):
        '''
        Test suite: 1
        Test case ID: 3
        '''
        loaddata = read_data("test1.arff.txt")
        #Extracted from function
        L = data_conversion(np.array(loaddata.iloc[:,-1])).astype(int)
        exp_labels = [0,1,0,1,0]
        self.assertEqual(L.tolist(), exp_labels)

    def test4(self):
        '''
        Test suite: 1
        Test case ID: 4
        '''
        loaddata = read_data("test2.arff.txt")
        #Extracted from function
        SM = np.array(loaddata.iloc[:,:-1]) 
        L = data_conversion(np.array(loaddata.iloc[:,-1])).astype(int)
        self.assertEqual(len(SM.tolist()), 125)
        self.assertEqual(len(L.tolist()), 125)

class main_test_2(unittest.TestCase):
    #Test suite 2
    def setUp(self):
        self.loaddata1 = read_data("test3.arff.txt")
        #Extracted from function
        SM = np.array(self.loaddata1.iloc[:,:-1]) 
        L = data_conversion(np.array(self.loaddata1.iloc[:,-1])).astype(int)
        self.data1 = [SM, L]
        self.loaddata2 = read_data("test2.arff.txt")
        #Extracted from function
        SM = np.array(self.loaddata2.iloc[:,:-1]) 
        L = data_conversion(np.array(self.loaddata2.iloc[:,-1])).astype(int)
        self.data2 = [SM, L]

    def test1(self):
        '''
        Test suite: 2
        Test case ID: 1
        '''
        try:
            feature_selection([True]*3, self.loaddata1, self.data1, 6, 5)
        except:
            assert False, "Feature selection failed for processed data"

    def test2(self):
        '''
        Test suite: 2
        Test case ID: 2
        '''
        try:
            feature_selection([True]*3, self.loaddata1, self.data1, 3, 4)
        except:
            assert False, "Feature selection failed for processed data"

    def test3(self):
        '''
        Test suite: 2
        Test case ID: 1
        '''
        try:
            feature_selection([False,True,False], self.loaddata1, self.data1, 4, 4)
        except:
            assert False, "Feature selection failed for processed data"

#====================( Main )====================
if __name__=='__main__':
    unittest.main()
