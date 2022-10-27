import pandas as pd
from sklearn import tree
from matplotlib import pyplot as plt
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