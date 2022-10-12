import string
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


path_a = '' 
filename_a = 'midterm_jeopardy_dataset.csv' #finding file
df_a = pd.read_csv(path_a + filename_a) #reading in the excel sheet


################################### Number 1 ###################################

temp_df = pd.DataFrame(df_a, columns = [' Category', ' Question', ' Value'])

temp_df["Total Value"] = temp_df[temp_df.columns[2:]].apply(lambda x: x.str[1:].str.split(',').str.join('')) #making a new column total value and making the strings more simple to turn to int
temp_df["Total Value"]= temp_df["Total Value"].replace(regex="one", value="0") #the string split weirdly turned values of "None" in the df to "one", so we have to replace that value to 0
temp_df["Total Value"] = temp_df["Total Value"].astype(float) #turning the whole column to float value


temp_df['Question Total'] = temp_df[' Question'].value_counts() # turning all the string into a value
temp_df['Question Total'] = temp_df['Question Total'].fillna(1) # value_counts() turned the values to NaN for some reason so here we make the NaN = 1
temp_df['Question Total'] = temp_df['Question Total'].astype(int) # the values showed as 5.0 which bothered me so I turned into int

temp_df = temp_df.groupby([' Category'])[['Question Total','Total Value']].sum() #grouping and summing


# Here I print out the categories with the most questions and values FIRST because the "Total Value" column is still an integer in this state
# at line 33 is when I change it back into a string to look like a currency, therefore not being able to use it for .idxmax()
print("\nCategories with the most total questions and most total value:\n")
maxValues = temp_df.idxmax()
print(maxValues)

temp_df["Total Value"] = temp_df["Total Value"].apply(lambda x: "${:.0f}".format((x))) #returning value column to currency
print(temp_df)



################################### Number 2 ###################################
path_b = '' 
filename_b = 'midterm_real_estate_dataset.csv' #finding file
df_b = pd.read_csv(path_b + filename_b) #reading in the excel sheet

x = df_b[['transaction date','house age','distance to the nearest MRT station', 'number of convenience stores']] # x vals
y = df_b[['house price of unit area']] # y vals
x_train, x_test,y_train,y_test = train_test_split(x,y,test_size =0.4) #splitting the data randomly 60/40 train/test
model = LinearRegression()
linear_model = model.fit(x_train,y_train) #fitting the model with the training set

# have the model predict y for all inputs, so we can evaluate r2 using the test set
linear_model_predict = linear_model.predict(x_test)
print("\nr2 score:", r2_score(y_test, linear_model_predict))
print("\nMSE:", mean_squared_error(y_test, linear_model_predict),"\n")

############ EVALUATION ############
#
# After calculating each r2 score the x attribute that is the least useful is teh transaction date,
# I found this out by taking the higest value of r2
# R2 value of:
# **** No transaction date = .65448 ****
# All 4 = .54056
# No number of convience stores = .46303
# No house age = .41931
# No distance to MRT = .388808
#
# P.S I could just have 5 linear regression model chunks of code that show each and then print out each but I felt that was redundant
# and didn't think the midterm question specified if I had to or not so I did it this way
#
####################################