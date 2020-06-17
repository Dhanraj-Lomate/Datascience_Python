#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:02:15 2020

@author: srinivasgurrala
"""

# Box and Whisker Plots
from matplotlib import pyplot
from pandas import read_csv
filename = "pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)

# Univariate Density Plots
from matplotlib import pyplot
from pandas import read_csv

data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
pyplot.show()


# Univariate Histograms
from matplotlib import pyplot
from pandas import read_csv

data.hist(figsize=(12,8))
pyplot.show()


# Scatterplot Matrix
from matplotlib import pyplot
from pandas import read_csv
from pandas.plotting import scatter_matrix

scatter_matrix(data)
pyplot.show()
