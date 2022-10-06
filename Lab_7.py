from matplotlib import test
import pandas as pd
from collections import Counter
import math
import operator
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn.preprocessing import MinMaxScaler
path = '' 
filename = 'haberman.csv' #finding file
df = pd.read_csv(path + filename) #reading in the excel sheet

#normalizing the data using min-max normalizing
#min-max was the only option because KNNClassifier doesn't like continous values and min-max gives discrete values
scaler = MinMaxScaler()
scaler.fit(df)
scaled = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled, columns=df.columns)


data = scaled_df.iloc[:,[0,1,2]] #taking first 3 columns as data (x)
survival = scaled_df.iloc[:,[3]] #taking the last column for survival rate (y)
x_train, x_test, y_train, y_test = train_test_split(data,survival, test_size=0.3, shuffle= True) #splitting into test and train data
train_df = pd.concat([x_train, y_train], axis=1) #combining to make a train and tes df
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

print("\nMy Accuracy:\n")
for k in range(1,16): # iterate through k=1 to k=10 as per requirements 
    right_answers= 0

    for testPoint in test_df.itertuples(index=False): #starting the iteration (or testing) of our testing data
        prediction = kNearestNeighbor(train_df, testPoint, k) # predicting the KNN
        if prediction == testPoint[3]: #adding the right predictions to get the accuracy
            right_answers +=1
    accuracy = "{:.2%}".format(right_answers/len(test_df)) #formatting the accuracy as a percent and printing it out
    print(accuracy)




########## SciKitLearn KNN ############
print('\nKNClassifer Accuracy:\n')
y_test = np.ravel(y_test) #raveling the data because the terminal doesn't like the dat conversion
y_train = np.ravel(y_train)
for k in range(1,16): # printing k 1-15 per requirements
    neigh = KNeighborsClassifier(k) #KNN function for each k value
    neigh.fit(x_train,y_train) #fitting the data
    predicted = neigh.predict(x_test) #predicting the y
    acc = accuracy_score(y_test, predicted)
    print("{:.2%}".format(acc))

############ Evaluation ################
#
# The accuracies are not the same
#
######################################
