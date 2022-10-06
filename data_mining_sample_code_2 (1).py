import pandas as pd

import xlsxwriter

filename = 'sample_input_data_2.csv'
data_frame_1 = pd.read_csv(filename) #reading all the data from the input file in one data frame

num_columns = len(data_frame_1.columns) #num of columns in the dataframe

wb = 'sample_output_data_2.xlsx'
wkb = xlsxwriter.Workbook(wb)
writer = pd.ExcelWriter(wb)

df_new = pd.DataFrame()# creating a new empty data frame
df_temp = data_frame_1.iloc[:,0] #extracting column 1 from the data_frame_1
df_new = pd.concat([df_new, df_temp], axis=1) #concatenating two dataframes

print(df_new)

df_temp = data_frame_1.iloc[:,1] #extracting column 2 from the data_frame_1
df_new = pd.concat([df_new, df_temp], axis=1) #concatenating two dataframes
print(df_new)

sheet_name = 1
sheetn = str(sheet_name)
worksheet = wkb.add_worksheet(sheetn) #adding a sheet in the output file named as "1"

df_new.to_excel(writer, sheetn, index = False) #writing the value of df_new in the sheet "1" of the output file

df_new = pd.DataFrame() #reinitializing df_new to an empty dataframe

df_temp = data_frame_1.iloc[:,2]
df_new = pd.concat([df_new, df_temp], axis=1)

df_temp = data_frame_1.iloc[:,3]
df_new = pd.concat([df_new, df_temp], axis=1)

sheet_name = 2
sheetn = str(sheet_name)
worksheet = wkb.add_worksheet(sheetn)

df_new.to_excel(writer, sheetn, index = False)

writer.save() #saving the output file

print(df_new)
