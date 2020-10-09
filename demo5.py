# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:33:56 2020

@author: Adewole
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('demo2.xlsx', 'Sheet1')
a = df['Time']
b = df['Temp']

# check the type of data class
print(type(df)) # dataframe
print(type(a)) # series
#plt.plot(a,b)

# extraction but it is still in dataframe class
e = df.iloc[0:24, 0:1]
f = df.iloc[0:24, 1:2]
print(e)
print(f)


df['Time'] = e
df['Temp'] = f
# change dataframe to series
g = df['Time']
h = df['Temp']
print(type(e))
print(type(g))
print(type(h))

print(g)
print(h)

i = g.astype('str')
j = h.astype('str')
print(i)
plt.plot(i,j)

