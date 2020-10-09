# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 11:42:08 2020

@author: Adewole
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('2014.xlsx', 'Aug')
a = df['Time']
b = df['Temperature']

# check the type of data class
#print(type(df)) # dataframe
#print(type(a)) # series
#plt.plot(a,b)

# extraction but it is still in dataframe class
e = df.iloc[0:24, 2:3]
f = df.iloc[0:24, 3:4]
print(e)
print(f)

ee = e.dropna(how='any')
ff = f.dropna(how='any')

print(ee)
#print(ff)

df['Time'] = ee
df['Temperature'] = f
# change dataframe to series
g = df['Time'].dropna(how='any')
h = df['Temperature']
print(type(ee))
print(g)
print(type(g))

#print(g)
#print(h)

i = g.astype('str')
j = h.astype('str')
#print(i)
#df.plot(kind="line", x = e, y = f)
#plt.plot(i,j)

