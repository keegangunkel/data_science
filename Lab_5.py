from matplotlib import test
import pandas as pd
from collections import Counter
import math
import operator
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

path = '' 
filename = 'haberman.csv' #finding file
df = pd.read_csv(path + filename) #reading in the excel sheet

#normalizing the data (z-score normalizing)
cols = list(df.columns)
for col in cols:
   df[col] = (df[col] - df[col].mean())/df[col].std() #normalizing the data to be all z-scores



data = df.iloc[:,[0,1,2]] # x attributes
survival = df.iloc[:,[3]] #y attributes
x_train, x_test, y_train, y_test = train_test_split(data,survival, test_size=0.3, random_state=1) #splitting the data into train and test, random state ensures the same split each time
train_df = pd.concat([x_train, y_train], axis=1) #concat into a train and test df
test_df = pd.concat([x_test, y_test], axis=1)

def euclideanDistance(trainingAttributes, testingAttributes, length): #distance formula that takes in the attributes
    distance = 0
    for x in range(length): # this loop is here to iterate through each attribute of each dataframe (mass - mass), (width-width), etc.
        distance += pow((trainingAttributes[x] - testingAttributes[x]), 2) 
    return math.sqrt(distance) 


def kNearestNeighbor(trainingSet, testingPoint, k): #knn formula that takes in the training set and the point we want to test
    distanceList = []
    for trainingPoint in trainingSet.itertuples(index=False):  #loops to make sure we get the distance in all the training df
        distance = euclideanDistance(trainingPoint, testingPoint, 3) # inputting the two points needed to get the distance
        distanceList.append((trainingPoint[3], distance)) #adding and sorting the labels with the distance
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

print("\nAccuracy:\n")
for k in range(1,11): # iterate through k=1 to k=10 as per requirements 

    right_answers = 0
    for testPoint in test_df.itertuples(index=False): #starting the iteration (or testing) of our testing data
        prediction = kNearestNeighbor(train_df, testPoint, k) # predicting the KNN
        if prediction == testPoint[3]: #adding the right predictions to get the accuracy
            right_answers +=1
    accuracy = "{:.2%}".format(right_answers/len(test_df)) #formatting the accuracy as a percent and printing it out
    yAxis.append(accuracy) #appending to list for graphing
    print(accuracy)


bar_graph = plt.scatter(xAxis, yAxis) #setting and showing graph
plt.show() 
