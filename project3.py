# -*- coding: utf-8 -*-

import random
import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Building block functions:


    
def dist(x1, x2):
    distance = 0
    for x in range(len(x1)): # this loop is here to iterate through each attribute of each dataframe (mass - mass), (width-width), etc.
        distance += pow((x1[x] - x2[x]), 2) 
    return math.sqrt(distance) 
#print(dist([0,0],[3,4]))
def centroid(xList):
    n = 2 # reconsider when using higher dimensional data
    sums = [0] *2
    for pt in xList:
        for ix in range(n):
            sums[ix] += pt[ix]

    for ix in range(n):
        sums[ix] = sums[ix]/len(xList)

    return sums

#print(centroid(testXList))
def assignmentDiffers(yCurrent, yPrev):
    return yCurrent != yPrev
#print(assignmentDiffers(x,y))
# Let's use a class for our K-Means implementation
class KMeans:
    """ Perform k-means clustering """
    
    def __init__(self, k=5):
        self.k = k          # number of clusters
        self.means = None   # means of clusters
    
    def __str__(self):
        return "KMeans(k=" + str(self.k) + ",means=" + str(self.means) + ")"
    
    def train(self, data):
        self.means = random.sample(data, k = self.k)
        
        oldAssignments = []
        while True:
            assignments = []
            for pt in data:
                distances= [dist(pt,m) for m in self.means]
                ix = distances.index(min(distances))
                assignments.append(ix)
            for clusterIndex in range(self.k):
                xList = []
                for ix in range(len(data)):
                    if assignments[ix] == clusterIndex:
                        xList.append(data[ix])  
                center = centroid(xList)
                self.means[clusterIndex] = center
            if not assignmentDiffers(assignments, oldAssignments):
                break
            oldAssignments = assignments
        return assignments
def variation(data, assignments, means):
    k = len(means)
    v = 0
    for pt,cluster in zip(data, assignments):
        d = dist(pt, means[cluster])
        v += d**2
    return v



def kmeans(filename):
    df = pd.read_csv(filename, header=None) #reading in the excel sheet
    data = df.iloc[:, [0,1]]
    data = data.values.tolist()
    varList = []
    for k in range(2,31):
        kobj = KMeans(k)
        assignments = kobj.train(data)
        var = variation(data,assignments, kobj.means)
        varList.append(var)
        xcoords = [pt[0]for pt in data]
        ycoords = [pt[1]for pt in data]
        sns.set(rc = {"figure.figsize":(10,10)})
        scatter = sns.scatterplot(x=xcoords, y = ycoords, hue= assignments, legend='full', palette='bright')
        fig = scatter.get_figure()
        fig.savefig(filename+'_cluster_graph_for_'+str(k)+'.png')
        plt.clf()

    line = sns.lineplot(data=varList)
    figLine = line.get_figure()

    figLine.savefig(filename+'_line_graph.png')
    

kmeans('clustering_dataset_01.csv')
kmeans('clustering_dataset_02.csv')
kmeans('clustering_dataset_03.csv')
                                
