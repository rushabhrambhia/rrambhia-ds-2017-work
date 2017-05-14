# -*- coding: utf-8 -*-
"""
Created on Thu May 11 12:26:16 2017

@author: rrambhia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score


df = pd.read_csv("../data/dailyFruitVeggie_drop_NaN_with_dummies.csv")

print df.columns

final_cols = ["_STATE","HD","dailyFruit","dailyVeggie","dailySmoker",
"exercise","single","ow_obese","hicholestrol","male","diabetic","nonSmoker","senior"]
df = df[final_cols]

df.shape

sns.heatmap(df.corr())


df.to_csv("../data/final_data_set.csv",index=False)