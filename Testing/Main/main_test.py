import sys
import unittest
sys.path.append("../../Program/Algorithm") #Adds directory containing jupyter import and module to test
import warnings # Suppress Warnings
from main_program import read_data, run, process_data, data_conversion, evaluate_data, run, feature_selection, model_creation, main_algo_run
#========== For tests setup ==========
from scipy.io import arff
from pf_eval.AUC_ROC import auc_roc_model
from pf_eval.F1_Score import f1_model
from pf_eval.Confusion_Matrix import confusion_matrix_model
import pandas as pd
import sklearn
import numpy as np

class main_test_1(unittest.TestCase):
    #Test suite 1

    def test1(self):
        '''
        Test suite: 1
        Test case ID: 1.1
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
        Test case ID: 1.2
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
        Test case ID: 1.3
        '''
        loaddata = read_data("test1.arff.txt")
        #Extracted from function
        L = data_conversion(np.array(loaddata.iloc[:,-1])).astype(int)
        exp_labels = [0,1,0,1,0]
        self.assertEqual(L.tolist(), exp_labels)

    def test4(self):
        '''
        Test suite: 1
        Test case ID: 1.4
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
        warnings.simplefilter('ignore')
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
            feature_selection([True]*3, self.loaddata1, self.data1, 6, 3)
        except:
            assert False, "Feature selection failed for processed data"

    def test2(self):
        '''
        Test suite: 2
        Test case ID: 2
        '''
        res = feature_selection([False, True, False], self.loaddata1, self.data1, 6, 3)
        assert len(res) == 1, "Feature selection failed to select the appropriate feature selection techniques (Single)"

    def test3(self):
        '''
        Test suite: 2
        Test case ID: 3
        '''
        res = feature_selection([False,True, True], self.loaddata1, self.data1, 6, 3)
        assert len(res) == 2, "Feature selection failed to select the appropriate feature selection techniques (Multiple)"

    def test4(self):
        '''
        Test suite: 2
        Test case ID: 4
        '''
        res = feature_selection([True, False, False], self.loaddata1, self.data1, 6, 4) #The fold argument was set to 4
        for r in res:
            assert len(r[0]) == 4 and len(r[1]) == 4, "Feature selection's K-fold argument failed to be read by the preprocessing algorithm"

    def test5(self):
        '''
        Test suite: 2
        Test case ID: 5
        '''
        res = feature_selection([True]*3, self.loaddata1, self.data1, 3, 3) #The train argument was set 3
        for r in res[1:3]:
            assert len(r[0][0][0]) == 3 , "Feature selection's training argument failed to be read by the preprocessing algorithm"

    def test6(self):
        '''
        Test suite: 2
        Test case ID: 6
        '''
        res = feature_selection([True]*3, self.loaddata1, self.data1, 6, 10000)
        assert res[0]==False and res[1]==1, "Feature selection failed to handle invalid k-fold argument"
    
    def test7(self):
        '''
        Test suite: 2
        Test case ID: 7
        '''
        res = feature_selection([True]*3, self.loaddata1, self.data1, 10000, 3)
        assert res[0]==False and res[1]==2, "Feature selection failed to handle invalid train argument"
    
    def test8(self):
        '''
        Test suite: 2
        Test case ID: 8
        '''
        try:
            feature_selection([True]*3, self.loaddata2, self.data2, 6, 3)
        except:
            assert False, "Feature selection failed for processed data on actual dataset"

class main_test_3(unittest.TestCase):
    #Test suite 3
    def setUp(self):
        warnings.simplefilter('ignore')
        loaddata1 = read_data("test3.arff.txt")
        #Extracted from function
        SM = np.array(loaddata1.iloc[:,:-1]) 
        L = data_conversion(np.array(loaddata1.iloc[:,-1])).astype(int)
        data1 = [SM, L]
        self.all_data = feature_selection([True,False,False], loaddata1, data1, 6, 3)[0]
        self.cfs_data = feature_selection([False,True,False], loaddata1, data1, 6, 3)[0]
        self.rfe_data = feature_selection([False,False,True], loaddata1, data1, 6, 3)[0]

    def test1(self):
        '''
        Test suite: 3
        Test case ID: 1
        '''
        try:
            data = [self.all_data[0][0], self.all_data[0][2]]
            model_creation([0,1,2,3,4], [0,1,2], data)
        except:
            assert False, "Model creation failed to fit data with all its original metrics"
    
    def test2(self):
        '''
        Test suite: 3
        Test case ID: 2
        '''
        try:
            data = [self.cfs_data[0][0], self.cfs_data[0][2]]
            model_creation([0,1,2,3,4], [0,1,2], data)
        except:
            assert False, "Model creation failed to fit data reduced using CFS"
    
    def test3(self):
        '''
        Test suite: 3
        Test case ID: 3
        '''
        try:
            data = [self.rfe_data[0][0], self.rfe_data[0][2]]
            model_creation([0,1,2,3,4], [0,1,2], data)
        except:
            assert False, "Model creation failed to fit data reduced using RFE"
    
    def test4(self):
        '''
        Test suite: 3
        Test case ID: 4
        '''
        data = [self.rfe_data[0][0], self.rfe_data[0][2]]
        models = model_creation([0,3], [], data)
        check1 = isinstance(models[0], sklearn.naive_bayes.ComplementNB)
        check2 = isinstance(models[1], sklearn.neural_network.MLPClassifier)
        assert check1 and check2, "Model creation failed to build the correct base prediction models"
    
    def test5(self):
        '''
        Test suite: 3
        Test case ID: 5
        '''
        data = [self.rfe_data[0][0], self.rfe_data[0][2]]
        models = model_creation([], [0], data)
        check = isinstance(models[0], sklearn.ensemble.RandomForestClassifier)
        assert check, "Model creation failed to build the correct ensemble prediction models"
    
    def test6(self):
        '''
        Test suite: 3
        Test case ID: 6
        '''
        data = [self.all_data[0][0], self.all_data[0][2]]
        models = model_creation([0,1,2,3,4], [0,1,2], data)
        for m in models:
            assert hasattr(m, 'predict'), "One or more models from Model creation has no predict() function"
    
class main_test_4(unittest.TestCase):
    #Test suite 4
    def setUp(self):
        warnings.simplefilter('ignore')
        loaddata1 = read_data("test3.arff.txt")
        #Extracted from function
        SM = np.array(loaddata1.iloc[:,:-1]) 
        L = data_conversion(np.array(loaddata1.iloc[:,-1])).astype(int)
        data1 = [SM, L]
        fs_data = feature_selection([True,False,False], loaddata1, data1, 6, 3)[0]
        train = [fs_data[0][0],fs_data[0][2]]
        self.test_m = fs_data[0][1]
        self.test_l = fs_data[0][3]
        self.test_model = model_creation([1], [], train)[0]

    def test1(self):
        '''
        Test suite: 4
        Test case ID: 1
        '''
        try:
            evaluate_data(self.test_model, self.test_m, self.test_l)
        except:
            assert False, "Evaluation method fail to run"

    def test2(self):
        '''
        Test suite: 4
        Test case ID: 2
        '''
        res = evaluate_data(self.test_model, self.test_m, self.test_l)
        assert len(res)==4, "Evaluation method returns the wrong number of results"
    
    def test3(self):
        '''
        Test suite: 4
        Test case ID: 3
        '''
        res = evaluate_data(self.test_model, self.test_m, self.test_l)
        for i in range(len(res)):
            assert res[i]<=1 and res[i] >= 0, "Evaluation method returns incorrect results"

    def test4(self):
        '''
        Test suite: 4
        Test case ID: 4
        '''
        res = evaluate_data(self.test_model, self.test_m, self.test_l)
        exp_res = [] #Expected result
        exp_res.append(auc_roc_model(self.test_model, self.test_m, self.test_l))
        exp_res.append(f1_model(self.test_model, self.test_m, self.test_l))
        exp_res.extend(confusion_matrix_model(self.test_model, self.test_m, self.test_l))
        for i in range(len(exp_res)):
            assert exp_res[i]==res[i], "Evaluation method returns the correct results but in the wrong order"

class main_test_5(unittest.TestCase):
    #Test suite 5
    def setUp(self):
        warnings.simplefilter('ignore')

    def test1(self):
        '''
        Test suite: 5
        Test case ID: 1
        '''
        fs = [True, True, True]
        pred_res = {
            "base": [1,1,1,1,1],
            "ensemble": [1,1,1]
        }
        train_res = {
            "tt": 6,
            "kfold": 3
        }
        try:
            main_algo_run("test3.arff.txt",fs, pred_res ,train_res)
        except:
            assert False, "The test failed"

    def test2(self):
        '''
        Test suite: 5
        Test case ID: 2
        '''
        fs = [True, False, True]
        pred_res = {
            "base": [1,0,0,0,0],
            "ensemble": [0,0,0]
        }
        train_res = {
            "tt": 1,
            "kfold": 2
        }
        res = main_algo_run("test3.arff.txt",fs, pred_res ,train_res)
    
    def test3(self):
        '''
        Test suite: 5
        Test case ID: 3
        '''
        fs = [True, False, True]
        pred_res = {
            "base": [1,0,0,0,0],
            "ensemble": [0,0,0]
        }
        train_res = {
            "tt": 4,
            "kfold": 4
        }
        res = main_algo_run("test3.arff.txt",fs, pred_res ,train_res)
        assert res[0] == ['Complement Naive Bayes'], "Main algorithm failed to build the correct base models"

    def test4(self):
        '''
        Test suite: 5
        Test case ID: 4
        '''
        fs = [False, True, True]
        pred_res = {
            "base": [0,0,0,0,0],
            "ensemble": [1,0,0]
        }
        train_res = {
            "tt": 5,
            "kfold": 5
        }
        res = main_algo_run("test3.arff.txt",fs, pred_res ,train_res)
        assert res[0] == ['Random Forest'], "Main algorithm failed to build the correct ensemble models"
    
    def test5(self):
        '''
        Test suite: 5
        Test case ID: 5
        '''
        fs = [False, True, True]
        pred_res = {
            "base": [0,0,0,0,0],
            "ensemble": [1,1,1]
        }
        train_res = {
            "tt": '5',
            "kfold": '5'
        }
        try:
            res = main_algo_run("test3.arff.txt",fs, pred_res ,train_res)
        except:
            assert False, "Main program failed to handle string inputs for training settings"
    
    def test6(self):
        '''
        Test suite: 5
        Test case ID: 6
        '''
        fs = [True, False, True]
        pred_res = {
            "base": [1,0,0,0,0],
            "ensemble": [0,0,0]
        }
        train_res = {
            "tt": 4,
            "kfold": 4
        }
        res = main_algo_run("test3.arff.txt",fs, pred_res ,train_res)
        assert res[1] == ['All','RFE'], "Main algorithm failed to identify the correct feature selection methods to use"
    
    def test7(self):
        '''
        Test suite: 5
        Test case ID: 7
        '''
        fs = [False, True, True]
        pred_res = {
            "base": [0,0,0,0,0],
            "ensemble": [1,1,1]
        }
        train_res = {
            "tt": '1000',
            "kfold": '5'
        }
        res = main_algo_run("test3.arff.txt",fs, pred_res ,train_res)
        assert not res[0] and res[1] == 2,"Main algorithm failed to recognize invalid input for train size"

    def test8(self):
        '''
        Test suite: 5
        Test case ID: 8
        '''
        fs = [False, True, True]
        pred_res = {
            "base": [0,0,0,0,0],
            "ensemble": [1,1,1]
        }
        train_res = {
            "tt": '5',
            "kfold": '10000'
        }
        res = main_algo_run("test3.arff.txt",fs, pred_res ,train_res)
        assert not res[0] and res[1] == 1,"Main algorithm failed to recognize invalid input for k-fold"

    def test9(self):
        '''
        Test suite: 5
        Test case ID: 9
        '''
        fs = [False, True, True]
        pred_res = {
            "base": [1,1,1,1,1],
            "ensemble": [1,1,1]
        }
        train_res = {
            "tt": '1',
            "kfold": '2'
        }
        try:
            res = main_algo_run("fail1.arff.txt",fs, pred_res ,train_res)
            assert not res[0] and res[1] == 0,"Main algorithm failed to recognize invalid dataset"
        except:
            pass
    
    def test10(self):
        '''
        Test suite: 5
        Test case ID: 10
        '''
        fs = [False, True, True]
        pred_res = {
            "base": [0,1,0,0,0],
            "ensemble": [1,0,1]
        }
        train_res = {
            "tt": '5',
            "kfold": '3'
        }
        try:
            mod_name, pp_name, res = main_algo_run("test3.arff.txt",fs, pred_res ,train_res)
            run(["Testfile"],"Testsavename",[res],mod_name,[pp_name])
            #Check the output folder to see if the csv was correctly created
        except:
            assert False, "Main algorithm failed to produce CSV file"

#====================( Main )====================
if __name__=='__main__':
    unittest.main()
