# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:29:39 2020

@author: Adewole
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('demo2.xlsx', 'Sheet1')
a = df['Time']
b = df['Temp']

print(df.dtypes)
print(a.dtypes)
plt.plot(a,b)
