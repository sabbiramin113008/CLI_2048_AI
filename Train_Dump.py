# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 12/23/2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

import pandas as pd
import warnings

from numpy import array

from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier as MLP
from sklearn.metrics import classification_report

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    File_Train = "train/tasbir.csv"
    file_name = File_Train.replace("train/", "").replace(".csv", "")
    df = pd.read_csv(File_Train)

    # Converting two different Dataframes
    # X = df.drop(['move'], axis=1)
    X = df.iloc[:, :-1]
    Y = df.iloc[:, -1]

    # Train Test Splitting
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.30)

    scale = StandardScaler()

    scale.fit(x_train)
    print("Scalling is Being Done")

    x_train = scale.transform(x_train)
    x_test = scale.transform(x_test)

    print(type(x_train))

    # clf = MLP(
    #     hidden_layer_sizes=(500, 50, 25, 10),
    #     activation="relu",
    #     solver="adam",
    #     max_iter=1000000,
    #     learning_rate_init=0.0001
    # )
    #
    # clf.fit(x_train, y_train)
    # joblib.dump(clf, "{}.sav".format(file_name))
    # predictions = clf.predict(x_test)
    # msg = (classification_report(y_test, predictions))
    # print(msg)

    row = [[16, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]]
    row = array(row)
    row = scale.transform(row)
    loaded_clf = joblib.load("{}.sav".format(file_name))
    predict_move = loaded_clf.predict(row)
    print(predict_move)
