# -*- coding: utf-8 -*-
"""
Created on Tue May 09 18:17:44 2017

@author: rrambhia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score


df = pd.read_csv("../data/dailyFruitVeggie_drop_NaN_with_dummies.csv")

df = df[df._STATE == 12]

df['weeklyFruit'] = df.dailyFruit * 7

df.boxplot(column="weeklyFruit", by="HD")
df.boxplot(column="dailyVeggie", by="HD")


# List of features
feature_cols = ["dailyFruit"]
X = df[feature_cols]
y = df.HD

print X.shape, y.shape

dtree = DecisionTreeClassifier()

scores = cross_val_score(dtree, X, y, cv=10, scoring='accuracy')
print scores

# Calculate null accuracy
print float(y.value_counts()[0])/len(y)

# Try predicting
dtree.fit(X,y)
y_pred = dtree.predict([[0]])
y_pred

pd.DataFrame({'feature':feature_cols, 'importance':dtree.feature_importances_})