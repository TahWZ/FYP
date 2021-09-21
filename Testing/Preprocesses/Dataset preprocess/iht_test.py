import sys
import unittest
import warnings # Suppress Warnings
sys.path.append("../../../Program/Algorithm/data_preproc") #Adds directory containing jupyter import and module to test
from IHT import iht
#========== For tests setup ==========
from scipy.io import arff
from sklearn.model_selection import train_test_split as ts
import pandas as pd
import numpy as np

class IHT_test(unittest.TestCase):
    
    def setUp(self):
        warnings.simplefilter('ignore')
        self.met1 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]
        self.lab1 = [0,1,1,1,1,1]

    def test1(self):
        #Test case ID: 1
        try:
            iht([self.met1,self.lab1], 2)
        except:
            assert False, "IHT failed when using valid data"

    def test2(self):
        #Test case ID: 2
        res = iht([self.met1,self.lab1], 2)
        check1 = len(res[0]) == len(res[1])
        check2 = isinstance(res[0][0],list)
        check3 = isinstance(res[1][0],int) 
        assert check1 and check2 and check3, "IHT failed to output data in the correct format"

    def test3(self):
        #Test case ID: 3
        res = iht([self.met1,self.lab1], 2)
        check1 = True
        for r in res[0]:
            if len(r)!=len(self.met1[0]):
                check1 = False
        assert check1, "IHT failed to output the undersampled metrics array correctly"
    
    def test4(self):
        #Test case ID: 4
        res1 = iht([self.met1,self.lab1], 0)
        res2 = iht([self.met1,self.lab1], 2)
        assert res1 != res2, "IHT failed to read k_fold argument correctly"

    def test5(self):
        #Test case ID: 5
        try:
            res = iht([self.met1,self.lab1], 0) 
            assert res[0] == self.met1 and res[1] == self.lab1, "IHT failed to handle invalid k_fold argument appropriately"
        except:
            assert False, "IHT failed to handle invalid k_fold argument appropriately"


#====================( Main )====================
if __name__=='__main__':
    unittest.main()
