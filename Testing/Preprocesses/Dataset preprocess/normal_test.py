import sys
import unittest
import warnings # Suppress Warnings
sys.path.append("../../../Program/Algorithm/data_preproc") #Adds directory containing Normalization function
from pp_tech.Normalization import Normalize
#========== For tests setup ==========
from scipy.io import arff
import pandas as pd
import numpy as np

def read_data(filename):
    data = arff.loadarff(filename)
    loaddata = pd.DataFrame(data[0])
    return loaddata

class Normal_test(unittest.TestCase):
    
    def setUp(self):
        warnings.simplefilter('ignore')
        self.data1 = read_data("test2.arff.txt")

    def test1(self):
        #Test case ID: 1
        try:
            output = Normalize(self.data1)
        except:
            assert False,"Normalization function fail to run"

    def test2(self):
        #Test case ID: 2
        loaddata = Normalize(pd.DataFrame([[0,1,2,3,4,5]]*20+[[]]*3))
        assert not loaddata.isnull().values.any(),"Normalization function fail to run"

    def test3(self):
        #Test case ID: 3
        loaddata = Normalize(pd.DataFrame([['a','b','c','d','e']]*20+[[]]*3))
        assert not loaddata.isnull().values.any() and len(loaddata) > 1,"Normalization fail to distinguish string and missing values"

    def test4(self):
        #Test case ID: 4
        try:
            output = Normalize(self.data1)
        except:
            assert False,"Normalization function fail to run"



#====================( Main )====================
if __name__=='__main__':
    unittest.main()
