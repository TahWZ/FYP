import unittest
import sys
sys.path.append("../../Program/Algorithm/pf_eval")
from AUC_ROC import auc_roc_model
from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

class AUC_Test(unittest.TestCase):

    def setUp(self):
        def data_conversion(data):
            for i in range(len(data)):
                if data[i] == b'N' or data[i] == b'false' or data[i] == b'no':
                    data[i] = 0
                else:
                    data[i] = 1
            return data
        self.model = LogisticRegression(solver='lbfgs',max_iter=10000000000)
        self.filename = 'KC1.arff.txt'
        self.data = arff.loadarff(self.filename)
        self.loaddata = pd.DataFrame(self.data[0])
        self.software_metrics = np.array(self.loaddata.iloc[:,:-1])
        self.labels = data_conversion(np.array(self.loaddata.iloc[:,-1]))
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.software_metrics, self.labels, test_size = 0.1)
        self.y_train = self.y_train.astype(int)
        self.y_test = self.y_test.astype(int)
        self.model = self.model.fit(self.X_train, self.y_train)

    def test1(self):
        result = auc_roc_model(self.model,self.X_test,self.y_test)

        # Checks if the result is a float
        self.assertIsInstance(result,float)

    def test2(self):
        X_test = [1,2,3]
        y_test = [1,2,3]

        # Passing a 1D array instead of 2D array
        with self.assertRaises(ValueError):
            auc_roc_model(self.model,X_test,y_test,test=True)

    def test3(self):
        X_test = [[1,2,3,4]]
        y_test = [1,2]

        # Inconsistent number of samples
        with self.assertRaises(ValueError):
            auc_roc_model(self.model,X_test,y_test,test=True)

    def test4(self):
        X_test = [[0,0,0,0]]
        y_test = [0,0,0,0]

        # One class present in y_test
        with self.assertRaises(ValueError):
            auc_roc_model(self.model,X_test,y_test,test=True)

    def test5(self):
        X_test = [[]]
        y_test = []

        # Empty test set
        with self.assertRaises(ValueError):
            auc_roc_model(self.model,X_test,y_test,test=True)

if __name__ == '__main__':
    unittest.main()

