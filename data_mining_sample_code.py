import pandas as pd

path = ''
filename = 'lab1_input_data.csv'
data_frame_1 = pd.read_csv(path + filename)



####calculating a sum of a column in a dataframe
sum_column_a = 0
sum_column_b = 0
for i in data_frame_1.index:
    sum_column_a = sum_column_a + data_frame_1.at[i,'column_a']
    sum_column_b = sum_column_b + data_frame_1.at[i, 'column_b']
print(sum_column_a)
print(sum_column_b)

print(data_frame_1['column_a'].sum())

####prints the sum of all the columns in a dataframe
print(data_frame_1.sum(axis = 0, skipna = True))

####will return a list of all the column headers
print(data_frame_1.columns)

####will return number of rows in a dataframe
print(len("The number of rows is:" + data_frame_1.index))

####will return the number of colums in the dataframe
print(len("The number of colums is:" + data_frame_1.columns))

####extracting data from a particular row in a dataframe

#adding a new column to a dataframe
data_frame_1['multiplication_of_a_and_b'] = 0.0
data_frame_1['multiplication_of_c_and_d'] = 0.0

####multiplying column values in a dataframe

data_frame_1['multiplication_of_a_and_b'] = data_frame_1['column_a'] * data_frame_1['column_b']
data_frame_1['multiplication_of_c_and_d'] = data_frame_1['column_c'] * data_frame_1['column_d']
print(data_frame_1)

####writing the dataframe to a csv file
data_frame_1.to_csv(path + 'lab1_output_data.csv', index = False, header = True)
