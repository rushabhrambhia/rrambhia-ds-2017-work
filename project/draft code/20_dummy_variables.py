# -*- coding: utf-8 -*-
"""
Created on Tue May 09 17:46:48 2017

@author: rrambhia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("../data/dailyFruitVeggie_drop_NaN.csv")

df.isnull().sum()

df['single'] = np.where(df.MARITAL==1,0,np.where(df.MARITAL==6,0,1))
df['diabetic'] = np.where(df.DIABETE3==1,1,np.where(df.DIABETE3==2,1,0))

df.single.value_counts()

df.DIABETE3.describe()

sns.heatmap(df.corr())

# List of features
feature_cols = ["dailyFruit","single"]

