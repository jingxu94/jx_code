# -*- coding: utf-8 -*-
"""
Created on Wed May 17 10:33:54 2017

@author: HP123
"""
'''kMeans
import numpy as np
from sklearn.cluster import KMeans
def loadData(filePath):
    fr = open(filePath,'r+')
    lines = fr.readlines()
    retData=[]
    retCityName = []
    for line in lines:
        items = line.strip().split(',')#文件预处理，划分名字和消费水平
        retCityName.append(items[0])
        retData.append([float(items[i]) for i in range(1,len(items))])
    return retData,retCityName
if __name__=='__main__':
    data,cityName = loadData('city.txt')
    km = KMeans(n_clusters=3)#聚成三类
    label = km.fit_predict(data)#打上相应标签
    expenses = np.sum(km.cluster_centers_,axis=1)#计算每一行的和（即每个类的消费水平）
    print(expenses)
    CityCluster = [[],[],[]]
    for i in range(len(cityName)):
        CityCluster[label[i]].append(cityName[i])#对应的标签中放入相应的城市名称
    for i in range(len(CityCluster)):
        print('Expenses:%.2f'% expenses[i])#输出每类消费水平
        print(CityCluster[i])
'''
import numpy as np
import sklearn.cluster as skc
from sklearn import metrics
import matplotlib.pyplot as plt


mac2id = dict()
onlinetimes = []
with open('TestData.txt',encoding = 'utf-8') as f:
    for line in f:
        mac = line.split(',')[2]#读取MAC地址
        onlinetime = int(line.split(',')[6])#读取上网时长
        starttime = int(line.split(',')[4].split(' ')[1].split(':')[0])#读取上网时间（小时）
        if mac not in mac2id:
            mac2id[mac] = len(onlinetimes)
            onlinetimes.append((starttime,onlinetime))
        else:
            onlinetimes[mac2id[mac]] = [(starttime,onlinetime)]
    real_X = np.array(onlinetimes).reshape((-1,2))#右对齐
x = real_X[:,0:1]
db = skc.DBSCAN(eps = 0.01,min_samples=20).fit(x)
labels = db.labels_
print('Lables:')
print(labels)
raito = len(labels[labels[:]==-1])/len(labels)
print('noise raito',format(raito,'.2%'))
n_clusters_ = len(set(labels))-(1 if -1 in labels else 0)
print('Estimated number of clusters:%d' % n_clusters_)
print('silhouette cofficient:%0.3f' % metrics.silhouette_score(x,labels))
for i in range(n_clusters_):
    print('cluster',i,':')
    print(list(x[labels == i].flatten()))
plt.hist(x,24)
x = np.log(1+real_X[:,1:])
db = skc.DBSCAN(eps = 0.14,min_samples = 10).fit(x)
labels = db.labels_
print('Lables:')
print(labels)
raito = len(labels[labels[:]==-1])/len(labels)
print('noise raito:',format(raito,'.2%'))
n_clusters_=len(set(labels))-(1 if -1 in labels else 0)
print('Estimated number of clusters:%d' % n_clusters_)
print('silhouette cofficient:%0.3f' % metrics.silhouette_score(x,labels))
for i in range(n_clusters_):
    print('cluster',i,':')
    cout = len(x[labels==i])
    mean = np.mean(real_X[labels == i][:,1])
    std = np.std(real_X[labels == i][:,1])
    print('\t number of sample:',cout)
    print('\t mean of sample:',format(mean,'.1f'))
    print('\t std of sample:',format(std,'.1f'))