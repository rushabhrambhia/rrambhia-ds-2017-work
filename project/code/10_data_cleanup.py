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

sns.heatmap(df.corr())

df.boxplot(column="_AGEG5YR")