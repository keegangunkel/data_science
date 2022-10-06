import pandas as pd

import xlsxwriter

filename = 'input_data_lab_2.csv'
data_frame_1 = pd.read_csv(filename) #reading all the data from the input file in one data frame

num_columns = len(data_frame_1.columns) #num of columns in the dataframe

wb = 'lab_2_output_data.xlsx'
wkb = xlsxwriter.Workbook(wb)
writer = pd.ExcelWriter(wb)

# INITAILIZING AND CREATING PAGE 1
page_1 = pd.DataFrame() #reinitializing df_new to an empty dataframe

counter =0
while(counter < 100):
    df_temp = data_frame_1.iloc[:,counter]#using the counter index to locate the correct columns to output
    page_1 = pd.concat([page_1, df_temp], axis=1)#concatenating two dataframes
    counter = counter + 1
    
sheet_name = 1
sheetn1 = str(sheet_name)
worksheet = wkb.add_worksheet(sheetn1) #adding a sheet in the output file named as "1"

# INITAILIZING AND CREATING PAGE 2

page_2 = pd.DataFrame() #reinitializing df_new to an empty dataframe
if(counter==100):
    counter =100
    while(counter < 200):
        df_temp = data_frame_1.iloc[:,counter]#using the counter index to locate the correct columns to output
        page_2 = pd.concat([page_2, df_temp], axis=1)#concatenating two dataframes
        counter = counter + 1
sheet_name = 2
sheetn2 = str(sheet_name)
worksheet = wkb.add_worksheet(sheetn2) #adding a sheet in the output file named as "2"

# INITAILIZING AND CREATING PAGE 3

page_3 = pd.DataFrame() #reinitializing df_new to an empty dataframe
if(counter==200):
    counter =200
    while(counter < 300):
        df_temp = data_frame_1.iloc[:,counter] #using the counter index to locate the correct columns to output
        page_3 = pd.concat([page_3, df_temp], axis=1)#concatenating two dataframes
        counter = counter + 1 
sheet_name = 3
sheetn3 = str(sheet_name)
worksheet = wkb.add_worksheet(sheetn3) #adding a sheet in the output file named as "3"

# INITAILIZING AND CREATING PAGE 4

page_4 = pd.DataFrame() #reinitializing df_new to an empty dataframe
if(counter==300):
    counter =300
    while(counter < 400):
        df_temp = data_frame_1.iloc[:,counter] #using the counter index to locate the correct columns to output
        page_4 = pd.concat([page_4, df_temp], axis=1)#concatenating two dataframes
        counter = counter + 1 
sheet_name = 4
sheetn4 = str(sheet_name)
worksheet = wkb.add_worksheet(sheetn4) #adding a sheet in the output file named as "4"

# INITAILIZING AND CREATING PAGE 5

page_5 = pd.DataFrame() #reinitializing df_new to an empty dataframe
if(counter==400):
    counter =400
    while(counter < 500):
        df_temp = data_frame_1.iloc[:,counter] #using the counter index to locate the correct columns to output
        page_5 = pd.concat([page_5, df_temp], axis=1)#concatenating two dataframes
        counter = counter + 1 
sheet_name = 5
sheetn5 = str(sheet_name)
worksheet = wkb.add_worksheet(sheetn5) #adding a sheet in the output file named as "5"


# INITAILIZING AND CREATING PAGE 6

page_6 = pd.DataFrame() #reinitializing df_new to an empty dataframe
if(counter==500):
    counter =500
    while(counter < 600):
        df_temp = data_frame_1.iloc[:,counter] #using the counter index to locate the correct columns to output
        page_6 = pd.concat([page_6, df_temp], axis=1)#concatenating two dataframes
        counter = counter + 1 
sheet_name = 6
sheetn6 = str(sheet_name)
worksheet = wkb.add_worksheet(sheetn6) #adding a sheet in the output file named as "6"

# INITAILIZING AND CREATING PAGE 7

page_7 = pd.DataFrame() #reinitializing df_new to an empty dataframe
if(counter==600):
    counter =600
    while(counter < 700):
        df_temp = data_frame_1.iloc[:,counter] #using the counter index to locate the correct columns to output
        page_7 = pd.concat([page_7, df_temp], axis=1)#concatenating two dataframes
        counter = counter + 1 
sheet_name = 7
sheetn7 = str(sheet_name)
worksheet = wkb.add_worksheet(sheetn7) #adding a sheet in the output file named as "7"

# INITAILIZING AND CREATING PAGE 8

page_8 = pd.DataFrame() #reinitializing df_new to an empty dataframe
if(counter==700):
    counter =700
    while(counter < 800):
        df_temp = data_frame_1.iloc[:,counter] #using the counter index to locate the correct columns to output
        page_8 = pd.concat([page_8, df_temp], axis=1)#concatenating two dataframes
        counter = counter + 1 
sheet_name = 8
sheetn8 = str(sheet_name)
worksheet = wkb.add_worksheet(sheetn8) #adding a sheet in the output file named as "8"

# INITAILIZING AND CREATING PAGE 9

page_9 = pd.DataFrame() #reinitializing df_new to an empty dataframe
if(counter==800):
    counter =800
    while(counter < 900):
        df_temp = data_frame_1.iloc[:,counter] #using the counter index to locate the correct columns to output
        page_9 = pd.concat([page_9, df_temp], axis=1)#concatenating two dataframes
        counter = counter + 1 
sheet_name = 9
sheetn9 = str(sheet_name)
worksheet = wkb.add_worksheet(sheetn9) #adding a sheet in the output file named as "9"

# INITAILIZING AND CREATING PAGE 10

page_10 = pd.DataFrame() #reinitializing df_new to an empty dataframe
if(counter==900):
    counter =900
    while(counter < 1000):
        df_temp = data_frame_1.iloc[:,counter] #using the counter index to locate the correct columns to output 
        page_10 = pd.concat([page_10, df_temp], axis=1)#concatenating two dataframes
        counter = counter + 1 
sheet_name = 10
sheetn10 = str(sheet_name)
worksheet = wkb.add_worksheet(sheetn10) #adding a sheet in the output file named as "10"






page_1.to_excel(writer, sheetn1, index = False)
page_2.to_excel(writer, sheetn2, index = False)
page_3.to_excel(writer, sheetn3, index = False)
page_4.to_excel(writer, sheetn4, index = False)
page_5.to_excel(writer, sheetn5, index = False)
page_6.to_excel(writer, sheetn6, index = False)
page_7.to_excel(writer, sheetn7, index = False)
page_8.to_excel(writer, sheetn8, index = False)
page_9.to_excel(writer, sheetn9, index = False)
page_10.to_excel(writer, sheetn10, index = False)

writer.save() #saving the output file

#print(df_new)
