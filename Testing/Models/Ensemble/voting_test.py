import sys
import unittest
sys.path.append("../../../Program/Algorithm/pred_mdls/ensemble")
from Voting import voting_model
from scipy.io import arff
import pandas as pd
import numpy as np

class Voting_test(unittest.TestCase):

    def setUp(self):
        '''
            Setting up the test environment
        '''
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
        software_metrices = np.array(loaddata1.iloc[:,:-1]) 
        labels = data_conversion(np.array(loaddata1.iloc[:,-1])).astype(int)
        self.data1 = [software_metrices, labels]

        data = arff.loadarff("test2.arff.txt")
        loaddata2 = pd.DataFrame(data[0])

        #Extracted from function
        software_metrices = np.array(loaddata2.iloc[:,:-1]) 
        labels = data_conversion(np.array(loaddata2.iloc[:,-1])).astype(int)
        self.data2 = [software_metrices, labels]

    def test1(self):
        '''
            Appropriate test size
        '''
        vt = voting_model(self.data1)
        test_set = [[0,0,0,1,1,1]]
        self.assertEqual(len(vt.predict(test_set)),1)

    def test2(self):
        '''
            Inappropriate test size
        '''
        vt = voting_model(self.data1)
        test_set = [[0,0,0,1,1]]

        # ValueError: X has 5 features per sample; expecting 6
        with self.assertRaises(ValueError):
            vt.predict(test_set)

    def test3(self):
        '''
            Different dimensions of test set
        '''
        vt = voting_model(self.data1)
        test_set = [0,0,0,1,1,1]

        # ValueError: Expected 2D array, got 1D array instead
        with self.assertRaises(ValueError):
            vt.predict(test_set)

    def test4(self):
        '''
            Empty test set
        '''
        vt = voting_model(self.data1)
        test_set = [[]]

        # ValueError: Found array with 0 feature(s) (shape=(1, 0)) while a minimum of 1 is required.
        with self.assertRaises(ValueError):
            vt.predict(test_set)

    def test5(self):
        '''
            Actual dataset

            self.data (KC1.arff.txt)
        '''
        vt = voting_model(self.data2)
        test_set = [[0,1]*20]

        self.assertEqual(len(vt.predict(test_set)),1)

if __name__ == '__main__':
    unittest.main()