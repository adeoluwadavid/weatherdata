# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:31:40 2020

@author: Adewole
"""
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.display import display
import ipywidgets as widgets
import pandas as pd
import matplotlib.pyplot as plt

def displayDropdown():
    widgetYear = widgets.Dropdown(
    options=['2014', '2015', '2016','2017','2018','2019','2020'],
    value='2014',
    description='Year:',
    disabled=False,
    )
    widgetMonth = widgets.Dropdown(
        options=['Jan', 'Feb', 'Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'],
        value='Jan',
        description='Month:',
        disabled=False,
    )
    widgetDay = widgets.Dropdown(
        options=[1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
        value=1,
        description='Day:',
        disabled=False,
    )
    widgetDataToPlot = widgets.Dropdown(
        options=['Temperature', 'Dew Point', 'Humidity','Wind', 'Wind Speed' ,'Wind Gust','Pressure','Precip','Condition'],
        value='Temperature',
        description='Data To Plot:',
        disabled=False,
    )
    display(widgetYear,widgetMonth,widgetDay,widgetDataToPlot)