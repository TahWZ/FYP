import sys
import unittest
sys.path.append("../../../Program/Algorithm/data_preproc")
from Preprocess import Normalize,K_fold,Stratifid_K_fold,IHT,data_conversion,preprocess
from CFS import cfs_algo
from RFE import rfe_algo
#========== For tests setup ==========
from scipy.io import arff
from sklearn.model_selection import train_test_split as ts
import pandas as pd
import numpy as np

# Suppresses all warnings
# ============================================
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
np.seterr(divide='ignore', invalid='ignore')
# ============================================

class Preprocess_Test(unittest.TestCase):

    def setUp(self):
        filename = 'test5.arff.txt'
        data = arff.loadarff(filename)
        self.loaddata = pd.DataFrame(data[0])
        self.loaddata = Normalize(self.loaddata)
        software_metrices = np.array(self.loaddata.iloc[:,:-1]) 
        labels = data_conversion(np.array(self.loaddata.iloc[:,-1])).astype(int)
        self.data = [software_metrices, labels]

    def test1(self):
        '''
            Fold = 3,4,5
        '''
        fold = 3
        result = preprocess(self.loaddata,fold)
        self.assertEqual(len(result),fold)

        fold = 4
        result = preprocess(self.loaddata,fold)
        self.assertEqual(len(result),fold)

        fold = 5
        result = preprocess(self.loaddata,fold)
        self.assertEqual(len(result),fold)

    def test2(self):
        '''
            Using CFS
        '''
        fold = 3
        train_size = 6
        cfs,selection = cfs_algo(self.data,train_size)
        result = preprocess(self.loaddata,fold,selection)
        self.assertEqual(len(result),fold)

    def test3(self):
        '''
            Using RFE
        '''
        fold = 3
        train_size = 6
        rfe,selection = rfe_algo(self.data,train_size)
        result = preprocess(self.loaddata,fold,selection)
        self.assertEqual(len(result),fold)

    def test4(self):
        '''
            K_fold > number of members in each size
        '''
        fold = 20
        # ValueError: n_splits=10 cannot be greater than the number of members in each class.
        with self.assertRaises(ValueError):
            preprocess(self.loaddata,fold)
        
    def test5(self):
        '''
            K fold > no_features
        '''
        fold = 20
        train_size = 6
        # ValueError: k should be >=0, <= n_features = 6; got 10. Use k='all' to return all features.
        cfs,selection = cfs_algo(self.data,train_size)
        with self.assertRaises(ValueError):
            preprocess(self.loaddata,fold,selection)

if __name__ == '__main__':
    unittest.main()
