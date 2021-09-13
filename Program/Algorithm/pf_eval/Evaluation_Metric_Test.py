import unittest
import warnings
from AUC_ROC import auc_roc_model
from F1_Score import f1_model
from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import numpy as np
import pandas as pd

class EvaluationMetricTest(unittest.TestCase):

    def setUp(self):
        self.model = LogisticRegression(solver='lbfgs',max_iter=10000000000)
        self.filename = 'KC1.arff.txt'
        self.data = arff.loadarff(self.filename)
        self.loaddata = pd.DataFrame(self.data[0])
        self.software_metrics = np.array(self.loaddata.iloc[:,:-1])
        self.labels = np.array(self.loaddata.iloc[:,-1])
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.software_metrics, self.labels, test_size = 0.1)
        self.y_train = self.y_train.astype('str')
        self.y_test = self.y_test.astype('str')
        self.model = self.model.fit(self.X_train, self.y_train)

    def test_auc_roc(self):
        result = auc_roc_model(self.model,self.X_test,self.y_test)

        # ======== Valid results ========= #
        # Checks if the result is a float
        self.assertIsInstance(result,float)

        # Checks if the result is not empty
        self.assertGreater(result,0)
        # ================================ #

        # ======= Invalid Results ======== #
        X_test = [1,2,3]
        y_test = [1,2,3]

        # Passing a 1D array instead of 2D array
        with self.assertRaises(ValueError):
            auc_roc_model(self.model,X_test,y_test)

        X_test = [[1,2,3,4]]
        y_test = [1,2]

        # Inconsistent number of samples
        with self.assertRaises(ValueError):
            auc_roc_model(self.model,X_test,y_test)

        X_test = [[0,0,0,0]]
        y_test = [0,0,0,0]

        # One class present in y_test
        with self.assertRaises(ValueError):
            auc_roc_model(self.model,X_test,y_test)

        X_test = [[0,0,0,0]]
        y_test = []

        # Empty y_test
        with self.assertRaises(ValueError):
            auc_roc_model(self.model,X_test,y_test)

        X_test = [[]]
        y_test = [0,0,0,1]

        # Empty X_test
        with self.assertRaises(ValueError):
            auc_roc_model(self.model,X_test,y_test)
        
        # =================================== #

    def test_f1_score(self):
        result = f1_model(self.model,self.X_test,self.y_test)

        y_pred = self.model.predict(self.X_test)

        # Check if the return result is a float type
        self.assertIsInstance(result,float)

        tn, fp, fn, tp = confusion_matrix(self.y_test, y_pred).ravel()
        if (((tp/(tp+fp))==0) or ((tp/(tp+fn))==0)):
            calculated_result = 0
        else:
            precision = (tp)/(tp+fp)
            recall = (tp)/(tp+fn)
            calculated_result = (2*precision*recall)/(precision+recall)

        # Check if f1-score is the same as calculated value
        self.assertEqual(result,calculated_result)

        # ======= Invalid Results ======== #
        X_test = [1,2,3]
        y_test = [1,2,3]

        # Passing a 1D array instead of 2D array
        with self.assertRaises(ValueError):
            f1_model(self.model,X_test,y_test)

        X_test = [[1,2,3,4]]
        y_test = [1,2]

        # Inconsistent number of samples
        with self.assertRaises(ValueError):
            f1_model(self.model,X_test,y_test)

        X_test = [[0,0,0,0]]
        y_test = [0,0,0,0]

        # One class present in y_test
        with self.assertRaises(ValueError):
           f1_model(self.model,X_test,y_test)

        X_test = [[0,0,0,0]]
        y_test = []

        # Empty y_test
        with self.assertRaises(ValueError):
            f1_model(self.model,X_test,y_test)

        X_test = [[]]
        y_test = [0,0,0,1]

        # Empty X_test
        with self.assertRaises(ValueError):
            f1_model(self.model,X_test,y_test)
        
        # =================================== #

if __name__ == '__main__':
    unittest.main()

