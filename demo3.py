# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:54:51 2020

@author: Adewole
"""

import pandas as pd
df = pd.read_excel('demo2.xlsx', 'Sheet1')

#print(df.dtypes)

a = df['Time']
b = df['Temp']


e = df.iloc[0:7, 0:1]
f = df.iloc[0:7, 1:2]

print(a)

c = pd.to_timedelta(a,unit='hour')

#plt.plot(e,f)
#print(f)
#print(e.dtypes)
#df.plot(kind="line", x = e, y = f)