import sys
import unittest
sys.path.append("../../../Program/Algorithm/data_preproc")
from fs_tech.CFS import cfs_algo
#========== For tests setup ==========
from scipy.io import arff
from sklearn.model_selection import train_test_split as ts
import pandas as pd
import numpy as np

class CFS_Test(unittest.TestCase):

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
        # Test if the selections is all True
        max_train = 6
        train_size = 6
        offset = max_train - train_size
        cfs,selections = cfs_algo(self.data1,train_size)
        test_selections = [True]*train_size+[False]*offset
        self.assertEqual(selections,test_selections)

    def test2(self):
        # Test if selection is 4 True and 2 False
        max_train = 6
        train_size = 4
        offset = max_train - train_size
        cfs,selections = cfs_algo(self.data1,train_size)
        test_selections = [True]*train_size+[False]*offset
        self.assertEqual(selections,test_selections)

    def test3(self):
        # Test if selection is all False
        max_train = 6
        train_size = 0
        offset = max_train - train_size
        cfs,selections = cfs_algo(self.data1,train_size)
        test_selections = [True]*train_size+[False]*offset
        self.assertEqual(selections,test_selections)

    def test4(self):
        # Test if train size is negative
        max_train = 6
        train_size = -1
        offset = max_train - train_size
        with self.assertRaises(ValueError):
            cfs,selections = cfs_algo(self.data1,train_size)

    def test5(self):
        # Test if train size is over maximum features
        max_train = 6
        train_size = 7
        offset = max_train - train_size
        with self.assertRaises(ValueError):
            cfs,selections = cfs_algo(self.data1,train_size)

if __name__ == '__main__':
    unittest.main()