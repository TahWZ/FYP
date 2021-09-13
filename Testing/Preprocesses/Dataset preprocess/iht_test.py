import sys
import unittest
sys.path.append("../../../Program/Algorithm/data_preproc") #Adds directory containing jupyter import and module to test
from IHT import iht
#========== For tests setup ==========
from scipy.io import arff
from sklearn.model_selection import train_test_split as ts
import pandas as pd
import numpy as np

class IHT_test(unittest.TestCase):
    
    def test1(self):
        #Test case ID: 1
        SM = [[5],[10]]*29
        SM.extend([[-10000],[-10000]])
        print(SM)
        SM = np.array(SM)
        L = np.array([[0],[1]]*30)
        data = [SM,L]
        self.assertEqual(len(SM), 60)
        SM, L = iht(data)
        self.assertLess(len(SM), 60)

    def test2(self):
        #Test case ID: 2
        data = [0]*21
        #3 Folds
        output = K_fold(data, f=3 ,read=False)
        self.assertEqual(sum(1 for _ in output), 3)
        #6 Folds
        output = K_fold(data, f=6 ,read=False)
        self.assertEqual(sum(1 for _ in output), 6)
        #9 Folds
        output = K_fold(data, f=9 ,read=False)
        self.assertEqual(sum(1 for _ in output), 9)

    def test3(self):
        #Test case ID: 3
        data = [0]*1
        output = K_fold(data, f=9 ,read=False)
        fail = False
        try:
            test = sum(1 for _ in output)
        except ValueError:
            pass
            fail = True
        self.assertTrue(fail)

    def test4(self):
        #Test case ID: 4
        filename = 'test.arff.txt'
        data = arff.loadarff(filename)
        loaddata = pd.DataFrame(data[0])
        data = np.array(loaddata)
        output = K_fold(data, read=False)
        self.assertEqual(sum(1 for _ in output), 10)



#====================( Main )====================
if __name__=='__main__':
    unittest.main()
