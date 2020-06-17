# Feature Importance with Extra Trees Classifier
from pandas import read_csv
from sklearn.ensemble import ExtraTreesClassifier
# load data
filename = '/Volumes/Data/Course Content/DS content/Tools/Python _Code/5.Feature Engineering/pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data= read_csv(filename, names=names)
array = data.values
X = array[:,0:8]
Y = array[:,8]
# feature extraction
model = ExtraTreesClassifier()

model.fit(X, Y)

print(model.feature_importances_)
