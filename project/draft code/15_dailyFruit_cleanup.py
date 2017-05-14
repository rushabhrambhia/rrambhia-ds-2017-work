# -*- coding: utf-8 -*-
"""
Created on Tue May 09 19:30:54 2017

@author: rrambhia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/brfss-data-subset_cleaned.csv")

df.shape

df.dailyFruit.describe()


# Technique 1: Impute dailyFruit using mode ie 2

df.dailyFruit.mode()
df_a = df
df_a["dailyFruit"].fillna(2, inplace=True)
df_a.dailyFruit.describe()
df_a = df_a[df_a.dailyFruit < 4.5]

df.to_csv("../data/dailyFruit_filled_mode_2.csv",index=False)

# Technique 2: Drop NaN
df.isnull().sum()
df_a = df[["dailyFruit","HD"]]
df_a = df_a.dropna()
df_a.head()
df_a.shape
df_a.isnull().sum()
df_a.dailyFruit.describe()
df_a = df_a[df_a.dailyFruit < 4.5]

df_a.to_csv("../data/dailyFruit_drop_na.csv",index=False)