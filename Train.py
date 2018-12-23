# -*- coding: utf-8 -*-
"""
author: S.M. Sabbir Amin
data: 12/23/2018
email: sabbir@rokomari.com, sabbiramin.cse11ruet@gmail.com

"""

import pandas as pd
import pickle
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

File_Train = "train/tasbir.csv"
df = pd.read_csv(File_Train)

df_copy = df.copy(deep=True)
X = df.drop(['move'], axis=1)
Y = df.iloc[:,16:]


print (Y.head(n=2))
