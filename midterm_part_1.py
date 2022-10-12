import string
import pandas as pd
import numpy as np


path = '' 
filename = 'midterm_jeopardy_dataset.csv' #finding file
df = pd.read_csv(path + filename) #reading in the excel sheet


################################### PART A ###################################

temp_df = pd.DataFrame(df, columns = [' Category', ' Question', ' Value'])

temp_df["Total Value"] = temp_df[temp_df.columns[2:]].apply(lambda x: x.str[1:].str.split(',').str.join('')) #making a new column total value and making the strings more simple to turn to int
temp_df["Total Value"]= temp_df["Total Value"].replace(regex="one", value="0") #the string split weirdly turned values of "None" in the df to "one", so we have to replace that value to 0
temp_df["Total Value"] = temp_df["Total Value"].astype(float) #turning the whole column to float value


temp_df['Question Total'] = temp_df[' Question'].value_counts() # turning all the string into a value
temp_df['Question Total'] = temp_df['Question Total'].fillna(1) # value_counts() turned the values to NaN for some reason so here we make the NaN = 1
temp_df['Question Total'] = temp_df['Question Total'].astype(int) # the values showed as 5.0 which bothered me so I turned into int

temp_df = temp_df.groupby([' Category'])[['Question Total','Total Value']].sum() #grouping and summing


# Here I print out the categories with the most questions and values FIRST because the "Total Value" column is still an integer in this state
# at line 33 is when I change it back into a string to look like a currency, therefore not being able to use it for .idxmax()
print("\n Categories with the most questions and most value:\n")
maxValues = temp_df.idxmax()
print(maxValues)

temp_df["Total Value"] = temp_df["Total Value"].apply(lambda x: "${:.0f}".format((x))) #returning value column to currency
print(temp_df)



################################### PART B ###################################