# from sklearn import neighbors
# from sklearn import datasets
#
# knn = neighbors.KNeighborsClassifier()
#
# iris = datasets.load_iris()
#
# knn.fit(iris.data,iris.target)
#
# PredictedLabel = knn.predict([[0.1,0.2,0.3,0.4]])
#
# print(PredictedLabel)
"""implement KNN :just try ; author:liao"""
import random
import csv
import math
import copy
######################################################
#load from Disk ,txt or csv and transform str to float
def loadDataSet(file,split,TrainSet=[],TestSet=[]):
    with open(file,mode='r') as f:
        dataList = list(f)

        for x in range(len(dataList)-1):
            data = dataList[x]
            dataList[x] = data.strip()

        print(dataList)
        dataList.remove('\n')
        print(dataList)

        for x in range(len(dataList)):
            data = dataList[x]
            data = data.split(',')
            for y in range(4):
                data[y] = float(data[y])
            if random.random() < split:
                TrainSet.append(data)
            else:
                TestSet.append(data)


#########################################################
#calculate instance's Euclidean distance
def InstanceCalc(InstanceA,InstanceB,Dimension):
    distance = 0;
    for x in range(Dimension):
        distance+=pow(InstanceA[x]-InstanceB[x],2)
    return math.sqrt(distance)

def takeEnd(elem):
    return elem[-1]
#########################################################
#get K neighbors of TestSet
def GetKNeighbors(TrainSet,TestSet,K):
    Neighbors = copy.deepcopy(TrainSet)
    K_Neigbors = []
    for x in range(len(TrainSet)):
            distance = InstanceCalc(TrainSet[x],TestSet,len(TestSet)-1)
            Neighbors[x].append(distance)
    # for x in range(len(Neighbors)-1):
    #     for y in range(x):
    #         if Neighbors[x][5]>Neighbors[y][5]:
    #             pass
    #         else:
    #             t = Neighbors[x]
    #             Neighbors[x] = Neighbors[y]
    #             Neighbors[y] = t
    Neighbors.sort(key=lambda ele:ele[5])
    for x in range(K):
        K_Neigbors.append(Neighbors[x])
    return K_Neigbors

#########################################################
#Neigbors Vote
def predictResult(Neigbors):
    Votes = {}
    for x in range(len(Neigbors)):
        classes = Neigbors[x][-2]
        if classes in Votes:
            Votes[classes]+=1
        else:
            Votes[classes] = 1
    return min(Votes,key=Votes.get)

#######################################################
#main
TrainSet = []
TestSet = []
split=0.67

loadDataSet(r'D:\深度神经网络算法全套\(基础2)机器学习深度学习基础\代码与素材(1)\02KNN\irisdata.txt',0.67,TrainSet,TestSet)



print("----------------test-----------------")
# K_Neigbors = GetKNeighbors(TrainSet,TestSet[0],7)
# print(K_Neigbors)
correct =[]
# print(predictResult(K_Neigbors))
print("TestSet:"+str(len(TestSet)))
print("TrainSet:"+str(len(TrainSet)))
for x in range(len(TestSet)):
    K_Neigbors = GetKNeighbors(TrainSet,TestSet[x],7)
    result = predictResult(K_Neigbors)
    print(str(x)+"--->"+"predict:"+str(result)+";"+"real:"+TestSet[x][-1])
    if result == TestSet[x][-1]:
        correct.append(result)
print((len(correct)/float(len(TestSet)))*100.0)