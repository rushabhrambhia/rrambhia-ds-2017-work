# -*- coding: utf-8 -*-
"""
Created on Tue May 09 19:14:10 2017

@author: rrambhia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/brfss-data-subset_cleaned.csv")


df.dailyFruit.mean()

df.boxplot(column="dailyFruit", by="HD")

df.plot.scatter("dailyFruit","HD")

sns.heatmap(df.corr())






