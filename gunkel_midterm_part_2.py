from matplotlib import test
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

path = '' 
filename = 'midterm_iris_dataset.xlsx' #finding file
df = pd.read_excel(path + filename) #reading in the excel sheet


data = df.iloc[:,[0,1,2,3]] #taking first 4 columns as data (x)
plant_type= df.iloc[:,[4]] #taking the last column for survival rate (y)
x_train, x_test, y_train, y_test = train_test_split(data,plant_type, test_size=0.3, shuffle= True) #splitting into test and train data

########## SciKitLearn KNN ############
y_test = np.ravel(y_test) #raveling the data because the terminal doesn't like the data conversion
y_train = np.ravel(y_train)
print('\nKNeighborsClassifer Accuracy:\n')
for k in range(1,11): # printing k 1-10 per requirements
    neigh = KNeighborsClassifier(k) #KNN function for each k value
    neigh.fit(x_train,y_train) #fitting the data
    predicted = neigh.predict(x_test) #predicting the y
    acc = accuracy_score(y_test, predicted)
    print("{:.2%}".format(acc))