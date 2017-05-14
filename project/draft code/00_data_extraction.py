# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 11:36:21 2017

@author: rrambhia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read sas file from BRFSS into a pandas dataframe
# I would advise not to read the entire file. 
# It took me 3 mins to read the whole file into a dataframe

df = pd.read_sas("C:/Users/rrambhia/Git/non-git/data for ds project/LLCP2015.XPT")
df.shape
df.head()
df.columns.values.tolist()

# create a subset of data frame with limited number of columns needed for project
features = ["_MICHD","SEX","MARITAL","EDUCA","_RFBMI5","_RACE_G1","DIABETE3","_RFCHOL","INCOME2","EXERANY2","SMOKDAY2","FRUIT1","FRUITJU1","_AGEG5YR"]
df_a = df[features]
df_a.head()
df_a.describe()
# exlude all rows with "no response" i.e Blank value in _MICHD
df_a = df_a[df_a._MICHD >= 1]

df_a.shape

# export df_a to a CSV for project purpose
df_a.to_csv("../data/brfss-data-subset.csv",index=False)
