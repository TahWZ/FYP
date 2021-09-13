import sys
import unittest
sys.path.append("../../../Program/Algorithm/data_preproc") #Adds directory containing jupyter import and module to test
from Kfold_cross_validation import K_fold
#========== For tests setup ==========
from scipy.io import arff
import pandas as pd
import numpy as np

class Kfold_test(unittest.TestCase):
    
    def test1(self):
        #Test case ID: 1
        data = [0]*20
        output = K_fold(data, read=False)
        self.assertEqual(sum(1 for _ in output), 10)

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
