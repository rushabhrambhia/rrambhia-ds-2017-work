# -*- coding: utf-8 -*-
"""
Created on Tue May 09 18:17:44 2017

@author: rrambhia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score


# Technique 1: Remove NaNs from dailyFruit
df = pd.read_csv("../data/dailyFruit_drop_na.csv")

# List of features
feature_cols = ["dailyFruit"]
X = df[feature_cols]
y = df.HD

print X.shape, y.shape

logReg = LogisticRegression()

scores = cross_val_score(logReg, X, y, cv=10, scoring='accuracy')
print scores

# Calculate null accuracy
print float(y.value_counts()[0])/len(y)

# Try predicting
logReg.fit(X,y)
logReg.predict_proba(X)
df_a["noHD_prob"] = logReg.predict_proba(X)[:, 0]
df_a.head()

# Plot probability against dailyFruit

plt.xlabel('dailyFruit')
plt.ylabel('household')
plt.scatter(df_a.dailyFruit, df_a.noHD_prob)
plt.plot(df_a.dailyFruit, df_a.noHD_prob, color='red')

# Technique 2: Impute dailyFruit using mode ie 1

df_a = pd.read_csv("../data/dailyFruit_filled_mode_2.csv")
# List of features
feature_cols = ["dailyFruit"]
X = df_a[feature_cols]
y = df_a.HD

print X.shape, y.shape

logReg = LogisticRegression()

scores = cross_val_score(logReg, X, y, cv=15, scoring='accuracy')
print scores

# Try predicting
logReg.fit(X,y)
y_pred = logReg.predict([[100]])
y_pred
# Calculate null accuracy
print float(y.value_counts()[0])/len(y)
