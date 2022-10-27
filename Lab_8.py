import pandas as pd
from sklearn import tree
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
path = '' 
filename = 'dataset_football_weather.xlsx' #finding file
df2 = pd.read_excel(path + filename) #reading in the excel sheet


##################### Part 1 #####################

# Replacing string values to 2,1,0 so we can make a DT
df2['Outlook'] = df2['Outlook'].replace(regex='Sunny', value=2)
df2['Outlook'] = df2['Outlook'].replace(regex='Overcast', value=1)
df2['Outlook'] = df2['Outlook'].replace(regex='Rain', value=0)
df2['Outlook'] = df2['Outlook'].astype(int)
# Replacing string values to 2,1,0 so we can make a DT
df2['Temperature'] = df2['Temperature'].replace(regex='Hot', value=2)
df2['Temperature'] = df2['Temperature'].replace(regex='Mild', value=1)
df2['Temperature'] = df2['Temperature'].replace(regex='Cool', value=0)
df2['Temperature'] = df2['Temperature'].astype(int)
# Replacing string values to 1,0 so we can make a DT
df2['Humidity'] = df2['Humidity'].replace(regex='High', value=1)
df2['Humidity'] = df2['Humidity'].replace(regex='Normal', value=0)
df2['Humidity'] = df2['Humidity'].astype(int)
# Replacing string values to 1,0 so we can make a DT
df2['Wind'] = df2['Wind'].replace(regex='Strong', value=1)
df2['Wind'] = df2['Wind'].replace(regex='Weak', value=0)
df2['Wind'] = df2['Wind'].astype(int)
# Replacing string values to 1,0 so we can make a DT
df2['Play'] = df2['Play'].replace(regex='Yes', value=1)
df2['Play'] = df2['Play'].replace(regex='No', value=0)
df2['Play'] = df2['Play'].astype(int)

# setting x and y for DT
x = df2[['Outlook','Temperature','Humidity','Wind']]
y = df2['Play']

# setting and fitting DT
dt = tree.DecisionTreeClassifier()
dt = dt.fit(x, y)
decision_tree = tree.plot_tree(dt)
                   
plt.show()
##################### EVALUATION #####################
#
# It does not match the one we generated in class,
# mainly because scikitlearn can only do a binary
# split tree. In class we did a "tri-split" 
# (we split by outlook -> sunny, overcast, rain)
#
######################################################


####################### Part 2 #######################

path = '' 
filename = 'haberman.csv' #finding file
df = pd.read_csv(path + filename) #reading in the excel sheet,

data = df.iloc[:,[0,1,2]] # x attributes
survival = df.iloc[:,[3]] #y attributes
x_train, x_test, y_train, y_test = train_test_split(data,survival, test_size=0.3, random_state=42) #splitting the data into train and test, random state ensures the same split each time
dt2 = tree.DecisionTreeClassifier(max_depth = 12, max_leaf_nodes=200,min_samples_leaf=1)
dt2 = dt2.fit(data, survival)
dt_score_train = dt2.score(x_train, y_train)
dt_score_test = dt2.score(x_test, y_test)
print("Decision tree training set accuracy:","{:.2%}".format(dt_score_train))
print("Decision tree test set accuracy:","{:.2%}".format(dt_score_test))





##################### EVALUATION #####################
#
# I did not get the expected 100% accuracy for the
# training set, the accuracy for the test set was 97.83%
#
# Accuracy[0] = patientAge, Accuraccy[1] = operationYear, Accuracy[2] = nodesDetected
# 
# Accuracy [0,1,2] = 97.83%
# Accuracy [0,1] = 91.30%
# Accuracy [0,2] = 88.04%
# Accuracy [1,2] = 84.78%
# Accuracy [2] = 76.09%
# Accuracy [0] = 72.83%
# Accuracy [1] = 71.74%
#
# The best combination (other than all 3) is, patientAge, operationYear
#
######################################################
