# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 20:05:42 2017

@author: rrambhia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/subset-fruit-veggies.csv")



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

def fvgreen2daily_veggie(row):
    if row['FVGREEN'] >= 100 and row['FVGREEN'] < 200:
        val = row['FVGREEN']-100
    elif row['FVGREEN'] >= 200 and row['FVGREEN'] < 300:
        val = (row['FVGREEN']-200)/7
    elif row['FVGREEN'] == 300:
        val = 0.02
    elif row['FVGREEN'] > 300 and row['FVGREEN']<400:
        val = (row['FVGREEN'] - 300)/30
    elif row['FVGREEN'] == 555:
        val = 0
    else: 
        val = float('NaN')
    return val

df['dailyFruit'] = df.apply(fruit2daily_fruit,axis = 1) 
df['dailyVeggie'] = df.apply(fvgreen2daily_veggie,axis = 1)

df.dailyFruit.describe()
df.dailyVeggie.describe()

df.isnull().sum()

df.to_csv("../data/calculated_dailyFruit_Veggie.csv",index=False)





