from matplotlib import test
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import math
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from cmath import sqrt
from sklearn.model_selection import KFold


path = '' 
filename = 'midterm_iris_dataset.xlsx' #finding file
df = pd.read_excel(path + filename) #reading in the excel sheet


years = df.iloc[:,[0]] #taking first column as x
salary= df.iloc[:,[1]] #taking second column as y
x_train, x_test, y_train, y_test = train_test_split(years,salary, test_size=0.3, shuffle= True) #splitting into test and train data 70/30
x_train2, x_test2, y_train2, y_test2 = train_test_split(years,salary, test_size=0.2, shuffle= True)#splitting into test and train data 80/20


#PART 1(1) AND PART 1(2)

#linear regression function
def linear_regression(x, y):     
    N = len(x)
    x_mean = x.mean()
    y_mean = y.mean()

    slope_num = ((x - x_mean) * (y - y_mean)).sum() 
    slope_den = ((x - x_mean)**2).sum()
    slope = slope_num / slope_den #slope equation
    
    y_int = y_mean - (slope*x_mean) #y-intercept equation

    r_val_num = ((x - x_mean) * (y - y_mean)).sum() 
    r_val_den = sqrt(((x - x_mean)**2).sum() * ((y - y_mean)**2).sum())
    r_val = r_val_num/r_val_den 
    r_val = r_val**2 #r-value equation

    reg_line = 'y = {}x + {}'.format(round(slope, 4), round(y_int, 4))
    
    return (y_int, slope,reg_line, r_val) #returning values

#prediction function
def predict(y_int, slope, new_x):  #predicting the y value on any given x 
    y = y_int + slope * new_x
    return y

#Arrays for the 70/30 split
x_train_array = x_train.to_numpy()
y_train_array = y_train.to_numpy()
x_test_array = x_test.to_numpy()
y_test_array = y_test.to_numpy()

#Arrays for the 80/20 split
x_train_array2 = x_train2.to_numpy()
y_train_array2 = y_train2.to_numpy()
x_test_array2 = x_test2.to_numpy()
y_test_array2 = y_test2.to_numpy()


predicted_list = [] # list for 70/30 split
predicted_list2 = [] #list for the 80/20 split
y_int, slope, reg_line, r_val = linear_regression(x_train_array, y_train_array) #regression for 70/30 split
y_int2, slope2, reg_line2, r_val2 = linear_regression(x_train_array2, y_train_array2) #regression for 80/20 split


for x in x_test_array: #iterating through the 70/30 split 
    manual_prediction = predict(y_int, slope, x.tolist()[0])#predicting each y for each x
    predicted_list.append(manual_prediction)#appending to a list to iterate through when calculating MSE


for x2 in x_test_array2: #same loop, but iterating through the 80/20 split
    manual_prediction2 = predict(y_int2, slope2, x2.tolist()[0]) 
    predicted_list2.append(manual_prediction2) 



def mean_squared_error_personal(y_test, prediction): #MSE definiton taking in two y values, (test and predicted)
    MSE_personal = 0
    for y1,y2 in zip(y_test, prediction): #zip works perfect for parallel arrays to grab each val at the same spot
        MSE_personal += ((y1 - y2)**2) #MSE equation


    return MSE_personal/len(y_test)

print("\nPersonal MSE for 70/30 split:", mean_squared_error_personal(y_test_array, predicted_list),'\n')
print("\nPersonal MSE for 80/20 split:",mean_squared_error_personal(y_test_array2, predicted_list2),'\n')



#PART 1(3)
model = LinearRegression()
linear_model = model.fit(x_train,y_train) #fitting the model with the training set

linear_model_predict = linear_model.predict(x_test) #predicting 

MSE = mean_squared_error(y_test, linear_model_predict) #MSE of the predicted and actual
RMSE = math.sqrt(MSE) 



## same exact code to get RMSE but for 80/20 split data set
model2 = LinearRegression()
linear_model2 = model2.fit(x_train2,y_train2)

linear_model_predict2 = linear_model2.predict(x_test2)

MSE2 = mean_squared_error(y_test2, linear_model_predict2)
RMSE2 = math.sqrt(MSE2)

#taking the personal MSE and squaring to get RMSE
RMSE_personal = sqrt(mean_squared_error_personal(y_test_array, predicted_list))
RMSE_personal2 = sqrt(mean_squared_error_personal(y_test_array2, predicted_list2))

#for some reason came out compelex, so turning each into a real number
RMSE_personal = RMSE_personal.real
RMSE_personal2 = RMSE_personal2.real

print("\nSciKit RMSE for a 70/30 split:", RMSE, '\n')
print("\nPersonal RMSE for 70/30 split:", RMSE_personal,'\n')
print("\nSciKit RMSE for a 80/20 split:", RMSE2, '\n')
print("\nPersonal RMSE for 80/20 split:", RMSE_personal2 ,'\n')

#PART 2(1)







