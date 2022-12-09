# -*- coding: utf-8 -*-

import random
import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Building block functions:

path = '' 
filename = 'clustering_dataset_01.csv' #finding file
df = pd.read_csv(path + filename, header=None) #reading in the excel sheet
data = df.iloc[:, [0,1]]
data = data.values.tolist()

    
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
varList = []
for k in range(2,31):
    kobj = KMeans(k)
    assignments = kobj.train(data)
    var = variation(data,assignments, kobj.means)
    varList.append(var)
xcoords = [pt[0]for pt in data]
ycoords = [pt[1]for pt in data]

print(var)
#sns.scatterplot(x=xcoords, y = ycoords, hue=assignments)
sns.lineplot(data=varList)
plt.show()
def kmeans(x, k):
    # Use it like this?
    km = KMeans(k = 10)
    km.train(x)
    # can print out km.means to see the fit means
    # can call km.classify([1,2,3,4]) to get cluster index
    
    #The function should return a list the length of x that contains
    # the cluster number (1 - k) for the corresponding x point
    # TODO determine return value



class DBSCAN:
    """ Perform DBSCAN clustering """
    
    def __init__(self, epsilon, minPts):
        self.epsilon = epsilon
        self.minPts = minPts
        
    def classify(self, x):
        """ Return the index of the cluster to which this point would belong, or None if it's an outlier """
        # TODO
        pass

    
    def train(self, data):
        """ Train model based on data """
        # Classify each point as a corePoint or not
        corePoints = [] # Contains either True or False for each point in data
        for pt1 in data:
            # Count points within self.epsilon from pt
            closePoints = 0
            for pt2 in data:
                if pt1 == pt2:
                    continue
                # Find distance, if < self.epsilon, increment closePoints
                d = dist(pt1, pt2)
                if d <= self.epsilon:
                    closePoints += 1
            if closePoints >= self.minPts:
                # pt1 is a core point!
                corePoints.append(True)
            else:
                # pt1 is not a core point!
                corePoints.append(False)
        # at this point, corePoints should contain True/False values
        
        clusterAssignments = [None] * len(data)
        nextClusterIndex = 0
        # loop here to generate cluster assignments
        # stop if all core points have been assigned to a cluster
        corePointsRemainUnassigned = True
        while (corePointsRemainUnassigned):
            # Randomly assign a remaining core point to be the first point in the next cluster
            unassignedCorePointIndices = []
            for pt1index in len(data):
                # check each point: if a corePoint and unassigned, add to unassignedCorePointIndices
                if corePoints[pt1index] == True and clusterAssignments[pt1index] == None:
                    unassignedCorePointIndices.append(pt1index)
            startingPointIndex = random.choice(unassignedCorePointIndicess)
            
            todoList = [] # will contain corePoints in our cluster, for which we need to find corePoint neighbors
            todoList.append(startingPointIndex)
            clusterAssignments[startingPointIndex] = nextClusterIndex
            
            # Then add other remaining core points within self.epsilon distance to the cluster
            # Continue adding nearby core points to grow the cluster
            # at this stage only add core points to the growing cluster
            while len(todoList) > 0:
                for pt1 in todoList:
                    # check for nearby core points, add them to our cluster and todo list
                    for pt2index in len(data):
                        pt2 = data[pt2index]
                        if pt1 == pt2:
                            continue
                        d = dist(pt1, pt2)
                        if d <= self.epsilon:
                            # this point is a neighbor
                            # if it's a core point, add it to our cluster and todo list
                            if corePoints[pt2index] == True:
                                todoList.append(pt2index)
                                clusterAssignments[pt2index] = nextClusterIndex
            
            # at this point, we have finished assigning core points to the cluster
            # Then add nearby non-core points to the growing cluster
            # These non-core points do not extend the cluster further
            for pt1index in len(data):
                pt1 = data[pt1index]
                if clusterAssignments[pt1index] == nextClusterIndex:
                    # check for unassigned non-corePoint neighbors
                    for pt2index in len(data):
                        if pt1 == pt2:
                            continue
                        pt2 = data[pt2index]
                        if clusterAssignments[pt2index] == None and corePoints[pt2index] == False:
                            if dist(pt1, pt2) < self.epsilon:
                                # this unassigned, non-core-point is close enough, assign to cluster
                                clusterAssignments[pt2index] = nextClusterIndex
                                
            # Now check if there are core points remaining that are unassigned
            # if so, set corePointsRemainUnassigned to False
            anyCorePointsRemainingUnassigned = False
            for pt1index in len(data):
                if corePoints[pt1index] == True and clusterAssignments[pt1index] == None:
                    anyCorePointsRemainingUnassigned = True
            if anyCorePointsRemainingUnassigned == False:
                corePointsRemainUnassigned = False
                                
