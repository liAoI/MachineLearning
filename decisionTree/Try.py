import csv

from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO
from sklearn.feature_extraction import DictVectorizer
filename = 'C:/Users/Administrator/Desktop/AllElectronics.csv'

# with open(filename,mode='r') as f:
f = open(filename,mode='r')
reader = csv.reader(f)
head = next(reader)
print(head)

featureList = []
labelList = []
for row in reader:
    labelList.append(row[len(row) - 1])
    rowDict = {}
    for i in range(1, len(row) - 1):
        rowDict[head[i]] = row[i]
    featureList.append(rowDict)
print(featureList)
print(labelList)

# Vectorize features
vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()
print(dummyX)
print("dummyX: " + str(dummyX))

lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print(dummyY)

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX,dummyY)
print(clf)
