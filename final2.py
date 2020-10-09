# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:16:17 2020

@author: Adewole
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('2017.xlsx', 'Feb')

# extraction but it is still in dataframe class
time = df.iloc[0:24, 2:3]
temperature = df.iloc[0:24, 3:4]
dewPoint = df.iloc[0:24, 4:5]
humidity = df.iloc[0:24, 5:6]
wind = df.iloc[0:24, 6:7]
windSpeed = df.iloc[0:24, 7:8]
windGust = df.iloc[0:24, 8:9]
pressure = df.iloc[0:24, 9:10]
precip = df.iloc[0:24, 10:11]
condition = df.iloc[0:24, 11:12]

#print(temperature)
#print(condition)
# save it back to the time and temperature

df['Time'] = time
df['Temperature'] = temperature
df['Dew Point'] = dewPoint
df['Humidity'] = humidity
df['Wind'] = wind
df['Wind Speed'] = windSpeed
df['Wind Gust'] = windGust
df['Pressure'] = pressure
df['Condition'] = condition

# change dataframe to series and the object to string
time1 = df['Time'].dropna(how='any').astype('str')
temperature1 = df['Temperature'].dropna(how='any').astype('str')
#condition1 = df['Condition'].dropna(how='any').astype('str')
#print(condition1)
#print(time1)
print(temperature1)
print(type(temperature1))
b = temperature1.str.extract(r'(^.{0,3})')
print(b)
print(type(b))

df['Temperature'] = b
temp2 = df['Temperature'].dropna(how='any').astype('str')
print(temp2)

temp3 = temp2.astype('float')
print(temp3)

plt.plot(time1,temp3)
