# -*- coding: utf-8 -*-
"""
Created on Tue May 09 18:17:44 2017

@author: rrambhia
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn import metrics

df_original = pd.read_csv("../data/final_data_set.csv")

#df_original = df_original[df_original.senior ==1]

#Undersampling to balance the data
sample_size = sum(df_original.HD == 1)*2
HD_indices = df_original[df_original.HD == 1].index
nonHD_indices = df_original[df_original.HD == 0].index
random_indices = np.random.choice(nonHD_indices, sample_size, replace=False)
df = df_original.loc[random_indices]
df = df.append(df_original.loc[HD_indices])



#Smaller subset of data
random_indices = np.random.choice(df_original.index, 4000, replace=False)
df = df_original.loc[random_indices]
#df = df_original

df = df[df.diabetic == 0]
df = df[df.ow_obese == 0]
df = df[df.hicholesterol == 0]

sns.heatmap(df.corr())
df.boxplot(column="dailyVeggie", by="HD")
df.boxplot(column="dailyFruit", by="HD")

# List of features
#feature_cols = ["dailyFruit","dailyVeggie","dailySmoker",
"exercise","single","ow_obese","hicholestrol","male","diabetic"]

feature_cols = ["dailyFruit","dailyVeggie"]
X = df[feature_cols]
y = df.HD

print X.shape, y.shape

scores_df = pd.DataFrame(columns = ("neighbors","metric"))

for i in range(1,10):
    knn = KNeighborsClassifier(n_neighbors= i)
    scores = cross_val_score(knn, X, y, cv=10, scoring='f1')
    scores_df.loc[i] = [i,scores.mean()]

print scores_df

print scores_df.loc[scores_df['metric'].idxmax()]

# Calculate null accuracy
print float(y.value_counts()[0])/len(y)

# Try predicting using train test split
knn = KNeighborsClassifier(n_neighbors= 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2)
knn.fit(X_train,y_train)    
y_pred_class = knn.predict(X_test)
#print metrics.accuracy_score(y_test, y_pred_class)

print metrics.recall_score(y_test, y_pred_class)

print metrics.confusion_matrix(y_test, y_pred_class)

#histogram
y_pred_prob = knn.predict_proba(X_test)[:, 1]

pred_pro = pd.DataFrame(knn.predict_proba(X_test))

Xpp = pd.concat([X_test,pred_pro],axis=1,join='inner')

# histogram of predicted probabilities
%matplotlib inline
plt.hist(y_pred_prob)
plt.xlim(0, 1)
plt.xlabel('Predicted probability of HD')
plt.ylabel('Frequency')

knn.predict([1,0.33])