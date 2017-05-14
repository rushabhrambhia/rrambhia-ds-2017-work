# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:09:46 2017

@author: rrambhia
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor


treereg = DecisionTreeRegressor(random_state=1)

# Technique 1: Remove NaNs from dailyFruit
df = pd.read_csv("../data/dailyFruitVeggie_drop_NaN_with_dummies.csv")

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