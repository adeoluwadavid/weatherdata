# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 17:15:15 2020

@author: Adewole
"""

a = '77 F'
b = a.split()
print(a)
print(b)

def myFunc(x):
    return 'F' != x

filtered = filter(myFunc, b)

for s in filtered:
    print(s)
    d = float(s)
    print(d)
#    print(type(s))
#    print(type(d))