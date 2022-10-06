# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 09:45:23 2022

@author: gunkeec
"""

from itertools import product
from multiprocessing.dummy import Array
from random import random
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '' 
filename = 'project_1_part_1.xlsx' #finding file


#Part 1a 
data_frame1 = pd.read_excel(path + filename) #reading in the excel sheet

order_quantity = data_frame1['Order Quantity'] #Reads in the order quantity data for the bar graph
product_type = data_frame1['Product'] #reads in product type for the bar graph
data_frame1 = data_frame1.groupby(['Product'])[['Order Quantity']].sum().reset_index()
print("\nTotal amount of each product sold:\n", data_frame1)
#Part 1a(a)

#starting the use of the matplotlib library to graph the data 
bar_graph = plt.barh(y=product_type ,width=order_quantity) #setting up the bar graph axis (axis are flipped so graph is horizontal)

#setting up graph title and labels
plt.title('Total pounds of Each Crop Harvested')
plt.ylabel('Type of crop')
plt.xlabel('Total pounds harvested')


#plt.show() #shows graph



#Part 1b

data_frame2 = pd.read_excel(path + filename)#new dataframe 

data_frame2 = data_frame2.groupby(['Lot code 1','Product'])[['Order Quantity']].sum().reset_index()#grouping the data by the lot code and product, then summing the order quantity of each product


print("\nTotal pounds of each crop harvested from each unique Lot code 1:\n", data_frame2)#printing out data frame


#Part 1c

data_frame3 = pd.read_excel(path + filename)#new dataframe

data_frame3 = data_frame3.groupby(['Customer'])[['Order Quantity']].sum().reset_index()#Grouping data by total pounds distributed by each customer


print("\nTotal pounds distributed to each unique customer:\n",data_frame3)#printing out data frame


#Part 1d

data_frame4 = pd.read_excel(path + filename)#new dataframe

data_frame4 = data_frame4.groupby(['Customer','Product'])[['Order Quantity']].sum().reset_index()#grouping data by total pounds of each crop sold by each customer


print("\nTotal pounds of each unique crop distributed to each unique customer\n", data_frame4)#printing out data frame


#Part 1e
data_frame5 = pd.read_excel(path + filename)#new dataframe

get_date = pd.to_datetime(data_frame5["Order ID"].str.slice(1,7), format="%m%d%y", errors = 'coerce')#grabbing the 'Order ID' Column and splicing the date out and turning it into x/x/xx format

data_frame5["Order Date"] = get_date #creating a new 'Order Date" column from the spliced 'Order ID' column

order_date_and_quantity = data_frame5.groupby(['Order Date'])[['Order Quantity']].sum().reset_index()#Grouping the new 'Order date' column with the sum of the order quantity





print("\nTotal pounds of each crop distributed each day of the year:\n", order_date_and_quantity)#printing out data frame

#Part 1e(a)

#X and Y variables for graphing
date = order_date_and_quantity['Order Date']
quantity = order_date_and_quantity['Order Quantity']

fig, ax = plt.subplots(figsize=(8, 6)) #Setting a figure variable to a subplot
ax.plot(date,quantity); #plotting x and y on the graph
plt.xlabel("Order Date")
plt.ylabel("Order Quantity")#graph labels
plt.title("Order Amount Per Day")
#plt.show() #shows graph

#Part 1f

data_frame6 = pd.read_excel(path + filename)#new dataframe



data_frame6 = data_frame6.groupby(['Harvest Date', 'Product'])[['Order Quantity']].sum().reset_index()#Grouping by harvest date, product, and order quantity

print("\nTotal pounds of each crop harvested each day of the year:\n", data_frame6)#printing dataframe

fig, ax1 = plt.subplots(figsize=(8, 6))#setting up variable for a graph


#for loop to loop in every plant 
for plant in product_type:

    ax1.plot('Harvest Date', 'Order Quantity', label =plant, data = data_frame6.where(data_frame6['Product']==plant).dropna())#here the biggest part is when I specify with the ".where" command

plt.xlabel("Harvest Date")
plt.ylabel("Amount")
plt.title("Product Order Amount on Each Harvest Date")
plt.legend() #shows the color line for each plant
#plt.show() #shows graph


#Part 1e

data_frame7 = pd.read_excel(path + filename)#new dataframe
product_money = data_frame7["Total Cost"].sum() #sums up the cost of all of the plants sold
currency = "${:,.2f}".format(product_money) #formats the product_money integer to look like $USD
print("\nTotal value of crops harvested:", currency) #prints the sum of the total cost column

#Part 1f

data_frame8 = pd.read_excel(path + filename)#new dataframe
total_products_sold = data_frame8["Order Quantity"].sum()
print("\nTotal number of products sold:", total_products_sold)


plt.show() #shows ALL graphs

