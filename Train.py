# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 12/23/2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from sklearn.neural_network import MLPClassifier as MLP
from sklearn.metrics import classification_report


def train_model(profile_name):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")

        file_train = "train/{}.csv".format(profile_name)
        file_name = profile_name
        df = pd.read_csv(file_train)

        X = df.iloc[:, :-1]
        Y = df.iloc[:, -1]

        x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30)
        print("Train-Test Split is Done")
        scale = StandardScaler()
        scale.fit(x_train)

        x_train = scale.transform(x_train)
        x_test = scale.transform(x_test)
        
        print("Training started....")

        clf = MLP(
            hidden_layer_sizes=(500, 50, 25, 10),
            activation="relu",
            solver="adam",
            max_iter=1000000,
            learning_rate_init=0.0001
        )
        print("Training Completed")

        clf.fit(x_train, y_train)
        joblib.dump(clf, "{}.sav".format(file_name))
        print("Model is Saved")
        predictions = clf.predict(x_test)
        msg = (classification_report(y_test, predictions))
        return msg

# def predict_move(boards)