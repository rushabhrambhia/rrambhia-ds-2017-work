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
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv("../data/final_data_set.csv")

df = df[df.diabetic == 0]
df = df[df.ow_obese == 0]
df = df[df.hicholestrol == 0]
df = df[df.senior ==1]
# df["dailyFruit"] = df.dailyFruit.round(1)

#df = df[(df.diabetic==0) | (df.hicholestrol==0) | (df.ow_obese==0)]
# List of features
# feature_cols = ["dailyFruit","dailyVeggie","diabetic","single","exercise","ow_obese","dailySmoker","hicholestrol"]  
feature_cols = ["dailyFruit"]
X = df[feature_cols]
y = df.HD

sns.heatmap(df.corr())

print X.shape, y.shape

logReg = LogisticRegression()

scores = cross_val_score(logReg, X, y, cv=10, scoring='f1')
print scores.mean()

# Calculate null accuracy
print float(y.value_counts()[0])/len(y)

# Try predicting using train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
logReg.fit(X_train,y_train)    
y_pred_class = logReg.predict(X_test)
print metrics.accuracy_score(y_test, y_pred_class)

print metrics.confusion_matrix(y_test, y_pred_class)

#histogram
y_pred_prob = logReg.predict_proba(X_test)[:, 1]

# histogram of predicted probabilities
%matplotlib inline
plt.hist(y_pred_prob)
plt.xlim(0, 1)
plt.xlabel('Predicted probability of HD')
plt.ylabel('Frequency')

