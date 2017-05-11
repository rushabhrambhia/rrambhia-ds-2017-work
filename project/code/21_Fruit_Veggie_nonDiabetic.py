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
df.diabetic.value_counts()

df.diabetic.describe()

sns.heatmap(df.corr())

df_a = df[df.diabetic==0]


df_a.shape
df_a.boxplot(column="dailyFruit", by="HD")
df_a.boxplot(column="dailyVeggie", by="HD")


df_a.to_csv("../data/dailyFruitVeggie_drop_NaN_non_diabetic.csv",index=False)

df.to_csv("../data/dailyFruitVeggie_drop_NaN_with_dummies.csv",index=False)