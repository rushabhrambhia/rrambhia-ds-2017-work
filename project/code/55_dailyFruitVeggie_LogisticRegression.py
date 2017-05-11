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


df = pd.read_csv("../data/dailyFruitVeggie_drop_NaN_with_dummies.csv")

df = df[df._STATE == 12]

df['weeklyFruit'] = df.dailyFruit * 7

df.boxplot(column="weeklyFruit", by="HD")
df.boxplot(column="dailyVeggie", by="HD")


# List of features
feature_cols = ["single"]
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
y_pred = logReg.predict([[1]])
y_pred

# Plot probability against dailyFruit
logReg.predict_proba(X)
df["noHD_prob"] = logReg.predict_proba(X)[:, 0]
df.head()
plt.xlabel('dailyFruit')
plt.ylabel('prob')
print plt.scatter(df_a.dailyFruit, df_a.noHD_prob)
print plt.plot(df_a.dailyFruit, df_a.noHD_prob, color='red')

