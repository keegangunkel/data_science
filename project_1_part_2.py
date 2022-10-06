"""
Created on Tues Sep 20 05:11:23 2022

@author: gunkeec
"""

from asyncio.windows_events import NULL
from cmath import nan
from functools import total_ordering
from locale import normalize
from operator import indexOf
from traceback import print_tb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as mp
path = '' 
filename = 'project_1_part_2.xlsx' #finding file

#Part 2a 


data_frame1 = pd.read_excel(path + filename) #reading in the excel sheet

veggie_total = data_frame1[['Basil', 'Beets','Bell Pepper','Broccoli','Brussels Sprouts','Carrots','Cauliflower','Cayenne Pepper','Cherry Tomatoes','Cilantro',	'Collards',	
'Garlic','Green Beans',	'Green Cabbage','Habanero Pepper','Head Lettuce','Jalapeño Pepper',	'Kale','Loose Leaf Lettuce','Muskmelon','Okra','Onions','Potatoes','Pumpkins',
'Radishes','Red Cabbage','Roma Tomatoes','Slicer Tomatoes','Swiss Chard','Tomatillos','Turnips','Watermelon','Winter Squash'
]].count() #counts all of the veggies in the dataframe
print("\nTotal aount of each crop sold:\n", veggie_total)
veggie_total=  veggie_total.sort_values(ascending= True)



#Part 2a(i)
y_values = veggie_total.values #grabs the values in the series and assigns it to the y-axis
x_values = veggie_total.index #grabs the index names in the series and assigns it to the x-axis
plt.barh(x_values,y_values) #assigns values to axis
plt.title('Total Votes for Each Crop')
plt.ylabel('Type of Crop')
plt.xlabel('Total Votes')
plt.show() #shows graph


#Part 2b
print("\nAmount of people that speak each language at each IP:\n")
lang_total = data_frame1["What Language Do You Speak?"].value_counts() #counts how many times each language comes up and assigns a value to the amount of times
data_frame2 = data_frame1.groupby(['User IP', "What Language Do You Speak?"])["User IP"].count() #groups the IP and language then counts the ip's for each language
print(data_frame2)

#Part 2b(i)
y_axis = lang_total.values #grabs the values in the series and assigns it to the y-axis
x_axis = lang_total.index #grabs the index names in the series and assigns it to the x-axis
plt.bar(x=x_axis, height=y_axis) #assigns values to axis
plt.title('Total Users of Each Language')
plt.ylabel('Total Users')
plt.xlabel('Language')
plt.show() #shows graph

#Part 2c
print("\nName, email, and IP of people who said yes to learning more:\n")
data_frame3 = data_frame1.loc[data_frame1["Would you like to learn more?"]=="Yes!"][["Name", "Email Address", "User IP"]] #locates whos says yes an puts all columns together
print(data_frame3)

#part 2d
ip_veggie_vote = pd.read_excel(path + filename)



#setting up the columns in the df
ip_veggie_vote = ip_veggie_vote[['User IP','Basil', 'Beets','Bell Pepper','Broccoli','Brussels Sprouts','Carrots','Cauliflower','Cayenne Pepper','Cherry Tomatoes','Cilantro',	'Collards',	
'Garlic','Green Beans',	'Green Cabbage','Habanero Pepper','Head Lettuce','Jalapeño Pepper',	'Kale','Loose Leaf Lettuce','Muskmelon','Okra','Onions','Potatoes','Pumpkins',
'Radishes','Red Cabbage','Roma Tomatoes','Slicer Tomatoes','Swiss Chard','Tomatillos','Turnips','Watermelon','Winter Squash']]

#replacing each vote with a value of one and null with a value of 0
ip_veggie_vote = ip_veggie_vote.replace(regex='Basil|Beets|Bell pepper|Broccoli|Brussels Sprouts|Carrots|Cauliflower|Cayenne Pepper|Cherry Tomatoes|Cilantro|Collards|Garlic|Green Beans|Green Cabbage|Habanero Pepper|Head Lettuce|Jalapeño Pepper|Kale|Loose Leaf Lettuce|Muskmelon|Okra|Onions|Potatoes|Pumpkins|Radishes|Red Cabbage|Roma Tomatoes|Slicer Tomatoes|Swiss Chard|Tomatillos|Turnips|Watermelon|Winter Squash', value=1)
ip_veggie_vote = ip_veggie_vote.fillna(value= 0)
#grouping by User IP and then summing the veggies to each IP
ip_veggie_vote = ip_veggie_vote.groupby('User IP')[['Basil', 'Beets','Bell Pepper','Broccoli','Brussels Sprouts','Carrots','Cauliflower','Cayenne Pepper','Cherry Tomatoes','Cilantro',	'Collards',	
'Garlic','Green Beans',	'Green Cabbage','Habanero Pepper','Head Lettuce','Jalapeño Pepper',	'Kale','Loose Leaf Lettuce','Muskmelon','Okra','Onions','Potatoes','Pumpkins',
'Radishes','Red Cabbage','Roma Tomatoes','Slicer Tomatoes','Swiss Chard','Tomatillos','Turnips','Watermelon','Winter Squash']].sum()
print("\nAmount of vegetable votes for each IP address:\n")
print(ip_veggie_vote)

#part 2e

toatal_veggie_vote = ip_veggie_vote.sum(axis=1)
print("\nAmount of total vegetable votes per for each IP address:\n")
print(toatal_veggie_vote)

#part 2f
ip_veggie_vote.loc[:,"Basil":"Winter Squash"] = ip_veggie_vote.loc[:,"Basil":"Winter Squash"].div(toatal_veggie_vote, axis=0) # dividing columns by the total votes columns
pct_vote_veggie = ip_veggie_vote.applymap(lambda x : "{:.2%}".format(x) if round(x,0) == x else "{:.1%}".format(x)) #apply map applies my lambda function across the data frame
print("\nPercentage of votes for each vegetable at each IP:\n")
print(pct_vote_veggie)

#Part 2g

sorted_pct = pd.DataFrame()
pd.options.display.max_columns = None
### this is a very messy way of showing the data because the index is the IP since I used the groupby method in the previous problems, thus trying to loop without the index
### would only sort the IP's in descending order, but it gets the job done.

for col in pct_vote_veggie: # iterate over columns
    df_tmp = pct_vote_veggie[col].to_frame().sort_values(by=col, ascending=False).reset_index().rename(columns={'index':'Crop'}) # converting each column to a dataframe and sorting the values 
    sorted_pct = pd.concat([sorted_pct, df_tmp], axis=1) # adds the temporary dataframes/columns and adds it to a new dataframe
print("\nPercentages in descending order:\n")
print(sorted_pct)


#Part 2h(d)


ip_language_vote = pd.read_excel(path + filename)

pd.options.display.max_columns = None

#setting up the columns in the df
ip_language_vote = ip_language_vote[['What Language Do You Speak?','Basil', 'Beets','Bell Pepper','Broccoli','Brussels Sprouts','Carrots','Cauliflower','Cayenne Pepper','Cherry Tomatoes','Cilantro',	'Collards',	
'Garlic','Green Beans',	'Green Cabbage','Habanero Pepper','Head Lettuce','Jalapeño Pepper',	'Kale','Loose Leaf Lettuce','Muskmelon','Okra','Onions','Potatoes','Pumpkins',
'Radishes','Red Cabbage','Roma Tomatoes','Slicer Tomatoes','Swiss Chard','Tomatillos','Turnips','Watermelon','Winter Squash']]

#replacing each vote with a value of one and null with a value of 0
ip_language_vote = ip_language_vote.replace(regex='Basil|Beets|Bell pepper|Broccoli|Brussels Sprouts|Carrots|Cauliflower|Cayenne Pepper|Cherry Tomatoes|Cilantro|Collards|Garlic|Green Beans|Green Cabbage|Habanero Pepper|Head Lettuce|Jalapeño Pepper|Kale|Loose Leaf Lettuce|Muskmelon|Okra|Onions|Potatoes|Pumpkins|Radishes|Red Cabbage|Roma Tomatoes|Slicer Tomatoes|Swiss Chard|Tomatillos|Turnips|Watermelon|Winter Squash', value=1)
ip_language_vote = ip_language_vote.fillna(value= 0)
#grouping by User IP and then summing the veggies- to each IP
ip_language_vote = ip_language_vote.groupby('What Language Do You Speak?')[['Basil', 'Beets','Bell Pepper','Broccoli','Brussels Sprouts','Carrots','Cauliflower','Cayenne Pepper','Cherry Tomatoes','Cilantro',	'Collards',	
'Garlic','Green Beans',	'Green Cabbage','Habanero Pepper','Head Lettuce','Jalapeño Pepper',	'Kale','Loose Leaf Lettuce','Muskmelon','Okra','Onions','Potatoes','Pumpkins',
'Radishes','Red Cabbage','Roma Tomatoes','Slicer Tomatoes','Swiss Chard','Tomatillos','Turnips','Watermelon','Winter Squash']].sum()
print("\nAmount of vegetable votes for each Language:\n")

print(ip_language_vote)


#part 2h(e)
ip_language_vote_total = ip_language_vote.sum(axis=1)

print("\nAmount of total vegetable votes per for each Language:\n")
print(ip_language_vote_total)


#part 2h(f)
pct_vote_language = pd.read_excel(path + filename)
ip_language_vote.loc[:,"Basil":"Winter Squash"] = ip_language_vote.loc[:,"Basil":"Winter Squash"].div(ip_language_vote_total, axis=0) # dividing columns by the total votes columns
pct_vote_language= ip_language_vote.applymap(lambda x : "{:.2%}".format(x) if round(x,0) == x else "{:.1%}".format(x)) #apply map applies my lambda function across the data frame
print("\nPercentage of votes for each vegetable at each IP:\n")
print(pct_vote_language)


#part 2h(g)
sorted_pct_language = pd.DataFrame()
pd.options.display.max_columns = None
### this is a very messy way of showing the data because the index is the IP since I used the groupby method in the previous problems, thus trying to loop without the index
### would only sort the IP's in descending order, but it gets the job done.

for col in pct_vote_veggie: # iterate over columns
    df_tmp_lang = pct_vote_language[col].to_frame().sort_values(by=col, ascending=False).reset_index().rename(columns={'index':'Crop'}) # converting each column to a dataframe and sorting the values 
    sorted_pct_language = pd.concat([sorted_pct_language, df_tmp_lang], axis=1) # adds the temporary dataframes/columns and adds it to a new dataframe
print("\nPercentages in descending order:\n")
print(sorted_pct)
