# -*- coding: utf-8 -*-
"""LinearRegressionMV_lesson2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TrFeBRl-yHd6KvkIxFORWmFL3W8eVK3C
"""

import pandas as pd
import numpy as np
from sklearn import linear_model

df=pd.read_csv('homeprices.csv')
df

import math
median_bedrooms=math.floor(df.bedrooms.median())
median_bedrooms

df.bedrooms=df.bedrooms.fillna(median_bedrooms)
df

df

df
reg=linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']],df.price)

reg.coef_

reg.intercept_

reg.predict([[3000,3,40]])

df=pd.read_csv('hiring.csv')
df

import math

# Criar o DataFrame
data = {
    'experience': [None, None, 'five', 'two', 'seven', 'three', 'ten', 'eleven'],
    'test_score(out of 10)': [8, 8, 6, 10, 9, 7, None, 7],
    'interview_score(out of 10)': [9, 6, 7, 10, 6, 10, 7, 8],
    'salary($)': [50000, 45000, 60000, 65000, 70000, 62000, 72000, 80000]
}
df = pd.DataFrame(data)

# Dicionário para converter texto em números
word_to_num = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
    'ten': 10, 'eleven': 11, 'twelve': 12
}

# Preencher valores ausentes e converter texto para números
df['experience'] = df['experience'].map(word_to_num)
df['experience'].fillna(0, inplace=True)  # Preenche NaN com 0
df['test_score(out of 10)'].fillna(df['test_score(out of 10)'].mean(), inplace=True)  # Média para valores ausentes

print(df)