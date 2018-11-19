import numpy
# from sklearn import svm
#
# x = [[2,0],[1,1],[2,3]]
# y = [0,0,1]
# clf = svm.SVC(kernel='linear')
# clf.fit(x,y)
#
# print(clf)
#from __future__ import print_function
a =numpy.mat([[-2/3,-2/3,-1/3],[-2/3,11/15,-2/15],[-1/3,-2/15,14/15]])
b =numpy.mat([[0,12,16],[12,288,309],[16,309,312]])
print(a)
print(a*b*a)