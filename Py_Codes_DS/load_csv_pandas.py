# Load CSV using Pandas
from pandas import read_csv
filename = '/Volumes/Data/Course Content/DS content/Tools/Python _Code/1.Load the data/pima-indians-diabetes.data.csv'
columns = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=columns)
print(data.shape)
data
