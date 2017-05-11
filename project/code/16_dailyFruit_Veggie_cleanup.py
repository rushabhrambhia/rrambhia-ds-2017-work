# -*- coding: utf-8 -*-
"""
Created on Tue May 09 19:30:54 2017

@author: rrambhia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/calculated_dailyFruit_Veggie.csv")

df.shape



# Technique 1: Drop dailyFruit and dailyVeggie NaN
df_a = df[df.dailyFruit >= 0]
df_a = df_a[df_a.dailyVeggie >= 0]
df_a = df_a[df_a.dailyFruit < 2.5]
df_a = df_a[df_a.dailyVeggie < 2]

df_a.boxplot(column="dailyFruit", by="HD")
df_a.boxplot(column="dailyVeggie", by="HD")

df_a.to_csv("../data/dailyFruitVeggie_drop_NaN.csv",index=False)