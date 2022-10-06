import pandas as pd

path = ''
filename = 'lab_1_input_data.csv'
data_frame_1 = pd.read_csv(path + filename)



####calculating a sum of a column in a dataframe
sum_column_a = 0
sum_column_b = 0


####will return number of rows in a dataframe
print("TOTAL NUMBER OF ROWS: " , len( data_frame_1.index))

####will return the number of colums in the dataframe
print("TOTAL NUMBER OF COLUMNS: ", len(data_frame_1.columns))

####extracting data from a particular row in a dataframe
####indexing of row starts from 0 and indexing of columns start from 0
#print(data_frame_1.iloc[365])

#adding a new column to a dataframe
data_frame_1['sales'] = 0.0

####multiplying column values in the dataframe to create the sales column

data_frame_1['sales'] = data_frame_1['quantity'] * data_frame_1['per_unit_price']

####printing the total number of sales by specific retailer
print("TOTAL NUMBER OF SALES BY ABC RETAILER: ", data_frame_1.groupby('retailer_name').sum().loc['ABC Retailer']['sales'])


####printing the total number of sales in a certain category by a certain retailer
print("TOTAL NUMBER OF VEGETABLE SALES BY ABC RETAILER: ", data_frame_1.groupby(['retailer_name' , 'category']).sum().loc[('ABC Retailer', 'Vegetables'),'sales'])


print("TOTAL NUMBER OF MEAT SALES BY XYZ RETAILER: ", data_frame_1.groupby(['retailer_name' , 'category']).sum().loc[('XYZ Retailer','Meat'), 'sales'])
#print(data_frame_1.groupby('category').sum())

####writing the dataframe to a csv file
data_frame_1.to_csv(path + 'output_report_lab_1.csv', index = False, header = True)
