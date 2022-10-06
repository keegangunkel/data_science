from asyncio.base_tasks import _task_print_stack
from msilib import knownbits
import pandas as pd
import numpy as np
import math
import operator
from collections import Counter
import matplotlib.pyplot as plt

path = '' 
filename = 'fruits_classification.xlsx' #finding file
df = pd.read_excel(path + filename) #reading in the excel sheet


#train and test datset with only the attributes we need
train_df = df[['mass','width','height','color_score','fruit_name']]
test_df = df[['mass','width','height','color_score','fruit_name']]

train_df=train_df.sample(frac=0.6) #taking a random sample of 60% the data frame
test_df=test_df.drop(train_df.index) #dropping the index to take the other 40%

# applying normalization (z-score)
for column in train_df.iloc[:,:-1]:
    train_df[column] = (train_df[column] -train_df[column].mean()) / train_df[column].std()

for column in test_df.iloc[:, :-1]:
    test_df[column] = (test_df[column] -test_df[column].mean()) / test_df[column].std()      
  

def euclideanDistance(trainingAttributes, testingAttributes, length): #distance formula that takes in the attributes
    distance = 0
    for x in range(length): # this loop is here to iterate through each attribute of each dataframe (mass - mass), (width-width), etc.
        distance += pow((trainingAttributes[x] - testingAttributes[x]), 2) 
    return math.sqrt(distance) 


def kNearestNeighbor(trainingSet, testingPoint, k): #knn formula that takes in the training set and the point we want to test
    distanceList = []
    for trainingPoint in trainingSet.itertuples(index=False):  #loops to make sure we get the distance in all the training df
        distance = euclideanDistance(trainingPoint, testingPoint, 4) # inputting the two points needed to get the distance
        distanceList.append((trainingPoint[4], distance)) #adding and sorting the labels with the distance
    distanceList.sort(key=operator.itemgetter(1)) 
    


    kItems = distanceList[:k] # since I dont need the whole list I specify just up to the k value
   
    kListLabels = []  #making and appending to a labels list to count
    for items in kItems: 
        kListLabels.append(items[0])
    
    counter = Counter(kListLabels)  #counter function to get the most common label
    most_common = counter.most_common(1)[0]
    most_common_label = most_common[0]  
    

    return most_common_label
    
# axis for graph
yAxis = []
xAxis = [1,2,3,4,5,6,7,8,9,10]

print("Accuracy:")
for k in range(1,11): # iterate through k=1 to k=10 as per requirements 
    right_answers= 0

    for testPoint in test_df.itertuples(index=False): #starting the iteration (or testing) of our testing data
        prediction = kNearestNeighbor(train_df, testPoint, k) # predicting the KNN
        if prediction == testPoint[4]: #adding the right predictions to get the accuracy
            right_answers +=1
    accuraccy = "{:.2%}".format(right_answers/len(test_df)) #formatting the accuracy as a percent and printing it out
    yAxis.append(accuraccy) #appending to list for graphing
    print(accuraccy)


bar_graph = plt.scatter(xAxis, yAxis) #setting and showing graph
plt.show() 

