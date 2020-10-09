# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:11:15 2020

@author: Adewole
"""

import matplotlib.pyplot as plt
import pandas as pd

# set directory

df = pd.read_excel('demo.xlsx', 'Sheet1')
#df['Time'] = pd.to_datetime(df['Time'])

# set plot

plt.plot(df['Time'].astype(str),df['Temperature'].astype(str))

# set label

plt.xlabel('time(hour)')
plt.ylabel('project')
plt.title('Keffi Weather')
plt.legend()

plt.show() 