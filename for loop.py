# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:43:05 2020

@author: Adewole
"""

import pandas as pd
df = pd.read_excel('demo.xlsx', 'Sheet1')

#print(df)


for i in range(len(df)):
    print(i)
    
print(type(df))

df.lookup('Time','Time')