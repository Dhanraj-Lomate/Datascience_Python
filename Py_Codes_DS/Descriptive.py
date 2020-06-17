# Class Distribution
from pandas import read_csv
filename = "C:\\Users\\Pooja Lomate\\Desktop\\Py_Codes_DS\\pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=names)


# Data Types for Each Attribute

types = data.dtypes
print(types)

# Statistical Summary
from pandas import read_csv
from pandas import set_option



set_option('precision', 3)
description = data.describe()
print(description)


# Pairwise Pearson correlations

correlations = data.corr(method='pearson')
print(correlations)

# Skew for each attribute

skew = data.skew()
print(skew)



class_counts = data.groupby('class').size()
print(class_counts)
