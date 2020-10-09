# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:03:46 2020

@author: Adewole
"""
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel('demo.xlsx', 'Sheet1')


#print(df['Time'])

#a=df[['Time']]
#print(a)
b = df[['Day','Hour','Time', 'Temperature']]
#print(b)

d = df.iloc[0:24, 2:3]

print(d)

e = df.iloc[0:24, 3:4]
print(e)

f = df.iloc[0:24, 2:4]
g = f.astype(str)
print(g)


#f.plot(kind='line', x ='Time', y='Temperature')
#plt.show()

g.plot(kind='bar', x ='Time', y='Temperature')
