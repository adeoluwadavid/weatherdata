# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:59:36 2020

@author: Adewole
"""


#import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

# set directory

df = pd.read_excel('demo2.xlsx', 'Sheet1')
z = pd.read_excel('2014.xlsx','Feb', header=0, usecols="A:C", skip_row=24,  skip_footer = 600)
print(z)
#dg = pd.read_excel('2014.xlsx','Feb', header=0, usecols="B:C", skip_footer=648)

#print(dg)

a = df['Time'].astype(str)
bb = df['Temp'].astype(str)
b = df['Temperature'].astype(str)
c= df['Dew Point'].astype(str)
d = df['Humidity'].astype(str)
e= df['Wind'].astype(str)
f = df['Wind Speed'].astype(str)
g = df['Wind Gust'].astype(str)
h = df['Pressure'].astype(str)
i = df['Precip'].astype(str)
j = df['Condition'].astype(str)


print(a.info())
#print(a)
#print(b)
#print(c)
#print(d)
#print(e)
#print(f)
#print(g)
#print(h)
#print(i)
#print(j)

plt.plot(a,b)

