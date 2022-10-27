import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np

path = '' 
filename = 'haberman.csv' #finding file
df = pd.read_csv(path + filename) #reading in the excel sheet,

data = df.iloc[:,[0,1,2]] # x attributes
survival = df.iloc[:,[3]] #y attributes
x_train, x_test, y_train, y_test = train_test_split(data,survival, test_size=0.3, random_state=42) #splitting the data into train and test, random state ensures the same split each time
dt = RandomForestClassifier(max_depth = 12, max_leaf_nodes=104,min_samples_leaf=1) #parameters to get the highest accuracy
survival = np.ravel(survival)
dt = dt.fit(data, survival) #fitting data
dt_score_train = dt.score(x_train, y_train) #getting accuracies
dt_score_test = dt.score(x_test, y_test)
print("\nRandom Forest training set accuracy:","{:.2%}".format(dt_score_train))
print("\nRandom Forest test set accuracy:","{:.2%}".format(dt_score_test))

reg = GradientBoostingRegressor(max_depth=11, max_leaf_nodes=75, min_samples_leaf=1) #parameters to get the highest accuracy

reg = reg.fit(data, survival) #fitting data
reg_score_train = reg.score(x_train, y_train) #getting accuracies
reg_score_test = reg.score(x_test, y_test)
print("\n\nRegressor tree training set accuracy:","{:.2%}".format(reg_score_train))
print("\nRegressor tree test set accuracy:","{:.2%}".format(reg_score_test))