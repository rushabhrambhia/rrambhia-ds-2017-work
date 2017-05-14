# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:05:42 2017

@author: rrambhia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/brfss-data-subset.csv")



df = df[(df._AGEG5YR >= 10) & (df._AGEG5YR < 14)]

df.shape

print(df.columns)

df.describe()

df['HD'] = np.where(df['_MICHD']==1, 1, 0)


def fruit2daily_fruit(row):
    if row['FRUIT1'] >= 100 and row['FRUIT1'] < 200:
        val = row['FRUIT1']-100
    elif row['FRUIT1'] >= 200 and row['FRUIT1'] < 300:
        val = (row['FRUIT1']-200)/7
    elif row['FRUIT1'] == 300:
        val = 0.02
    elif row['FRUIT1'] > 300 and row['FRUIT1']<400:
        val = (row['FRUIT1'] - 300)/30
    elif row['FRUIT1'] == 555:
        val = 0
    else: 
        val = float('NaN')
    return val

def fruit_juice2daily_fruit(row):
    if row['FRUITJU1'] >= 100 and row['FRUITJU1'] < 200:
        val = row['FRUITJU1']-100
    elif row['FRUITJU1'] >= 200 and row['FRUITJU1'] < 300:
        val = (row['FRUITJU1']-200)/7
    elif row['FRUITJU1'] == 300:
        val = 0.02
    elif row['FRUITJU1'] > 300 and row['FRUITJU1']<400:
        val = (row['FRUITJU1'] - 300)/30
    elif row['FRUITJU1'] == 555:
        val = 0
    else: 
        val = float('NaN')
    return val

df['dailyFruit'] = df.apply(fruit2daily_fruit,axis = 1) + df.apply(fruit_juice2daily_fruit,axis = 1)

df.dailyFruit.describe()

df.isnull().sum()

df.to_csv("../data/brfss-data-subset_cleaned.csv",index=False)





