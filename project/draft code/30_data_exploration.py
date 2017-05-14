# -*- coding: utf-8 -*-
"""
Created on Thu May 11 12:45:10 2017

@author: rrambhia
"""

# Data Exploration

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/final_data_set.csv")

df.groupby(df.HD).sum()/df.groupby(df.HD).count()*100


df.dailyFruit.head