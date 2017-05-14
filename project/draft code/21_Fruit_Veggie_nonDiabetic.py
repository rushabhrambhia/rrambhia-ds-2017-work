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

df = df[df._AGEG5YR < 14]

df.isnull().sum()

#df = df[df.SMOKDAY2 > 0]
df = df[df._RFCHOL > 0]
df = df[df.EXERANY2 > 0]

df.shape


df['single'] = np.where(df.MARITAL==1,0,np.where(df.MARITAL==6,0,1))
df['diabetic'] = np.where(df.DIABETE3==1,1,np.where(df.DIABETE3==2,1,0))
df['male'] = np.where(df.SEX == 1,1,0)
df['hicholestrol'] = np.where(df._RFCHOL == 2, 1, 0)
df['ow_obese'] = np.where(df._RFBMI5 == 2, 1, 0)
df['exercise'] = np.where(df.EXERANY2 == 1, 1, 0)
df['senior'] = np.where(df._AGEG5YR >= 10, 1, 0)


#df['dailySmoker'] = np.where(df.SMOKDAY2 == 1, 1, 0)
#df['nonSmoker'] = np.where(df.SMOKDAY2 == 3, 1, 0)
df.single.value_counts()
df.diabetic.value_counts()
df.male.value_counts()

df.diabetic.describe()


df = df[df.senior==1]

sns.heatmap(df.corr())



df.shape
df.boxplot(column="dailyVeggie", by="HD")
df.boxplot(column="dailyFruit", by="HD")


df_a.to_csv("../data/dailyFruitVeggie_drop_NaN_non_diabetic.csv",index=False)

df.to_csv("../data/dailyFruitVeggie_drop_NaN_with_dummies.csv",index=False)