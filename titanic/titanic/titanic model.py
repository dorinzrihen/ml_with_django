#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib as plt

df = pd.read_csv("train.csv")

df["Age"].fillna(df["Age"].median(),inplace=True)
df["Embarked"].fillna("S",inplace=True)
del df["Cabin"]

def get_title(name):
    if '.' in name:
        return name.split(",")[1].split('.')[0].strip()
    else:
        return "Unknown"
    
def replace_title(x):
    title = x["Title"]
    if title in ['Capt','Col','Major']:
        return 'Officer'
    elif title in ['Jonkheer','Don','the Countess','Dona','Lady','Sir']:
        return 'Royalty'
    elif title in ['the Countess','Lady','Mme']:
        return 'Mrs'
    elif title in ['Mlle','Ms']:
        return 'Miss'
    else:
        return title
    
    
df["Title"] = df["Name"].map(lambda x:get_title(x))
df["Title"] = df.apply(replace_title,axis=1)
df.drop("Ticket",axis=1,inplace=True)
df.Sex.replace(('male','female'),(0,1),inplace=True)
df.Embarked.replace(('S','C','Q'),(0,1,2),inplace=True)
df.Title.replace(('Mr','Miss','Mrs','Master','Dr','Rev','Officer','Royalty'),(0,1,2,3,4,5,6,7),inplace=True)
del df["Name"]

from sklearn.model_selection import train_test_split

x = df.drop(["Survived", "PassengerId"],axis=1)
y = df["Survived"]
x_train, x_val, y_train ,y_val = train_test_split(x,y, test_size = 0.1)

import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

randomforest = RandomForestClassifier()
randomforest.fit(x_train, y_train)
y_pred = randomforest.predict(x_val)
acc_randomforest = round(accuracy_score(y_pred, y_val)*100, 2)
print(acc_randomforest)


pickle.dump(randomforest, open('titanic_model.sav','wb'))


# In[ ]:




