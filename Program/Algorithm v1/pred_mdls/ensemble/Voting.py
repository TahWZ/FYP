#==== Imports ====#
import numpy as np
import pandas as pd
from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import VotingClassifier

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
#=================#

#==== Functions ====#
def voting_model(data, args=[1000]):
    logistic_regression = LogisticRegression(solver = 'lbfgs',max_iter=10000000000)
    random_forest = RandomForestClassifier(n_estimators = args[0])
    naive_bayes = GaussianNB()

    labels = ['Logistic Regression', 'Random Forest', 'Naive Bayes']

    # Change model here
    voting = VotingClassifier(estimators = [(labels[0],logistic_regression),
                                        (labels[1],random_forest),
                                        (labels[2],naive_bayes)],
                              voting='soft')

    voting.fit(data[0],data[1])
    return voting
#===================#