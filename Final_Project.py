import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import folium
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

filename = 'highest_earning_teams.csv' #finding file
df_teams = pd.read_csv(filename) #reading in the excel sheet

filename2 = 'highest_earning_players.csv' #finding file
df_players = pd.read_csv(filename2) #reading in the excel sheet

filename3 = 'country-and-continent-codes-list.csv' #finding file
df_country = pd.read_csv(filename3) #reading in the excel sheet


df_teams['TotalUSDPrize'] = df_teams['TotalUSDPrize'].astype('int64') # making money int so it prints nicer

top_earnings = df_teams.groupby(['Game'])['TotalUSDPrize'].sum().sort_values(ascending=False).reset_index()#grouping the game and earnings to graph
print(top_earnings,'\n')

genre_earnings = df_teams.groupby(['Genre'])['TotalUSDPrize'].sum().sort_values(ascending=False).reset_index()
print(genre_earnings,'\n'),

df_players["Name"] = df_players["NameFirst"] +" "+ df_players["NameLast"] +"("+df_players["CountryCode"]+")" #combining first and last name with the country code in parenthesis

top_earnings_players = df_players.groupby(['Name'])['TotalUSDPrize'].sum().sort_values(ascending=False).reset_index()#grouping the player and earnings to graph
top_earnings_players = top_earnings_players.nlargest(10, 'TotalUSDPrize')
print(top_earnings_players)






#bar graph team earnings
plt.figure(figsize=(20,10)) #setting fig size to fit all the data
sns.barplot(x=top_earnings['Game'], y=top_earnings['TotalUSDPrize']) # x and y axis
plt.title('Highest Earning Games', size=25) 
plt.ylabel('Total Prize Money (USD)(100 Millions)', size = 17)
plt.xticks(rotation=15)
plt.xlabel('Games', size=17)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# pie chart team earnings
plt.figure(figsize=(12,10))
plt.pie(top_earnings['TotalUSDPrize'], labels=top_earnings['Game'], autopct='%.2f')
plt.title('Pie Chart: Highest Prize Earnings by Game', size = 25)
plt.axis('equal')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)


#pie chart genre earnings
plt.figure(figsize=(12,10))
plt.pie(genre_earnings['TotalUSDPrize'], labels=genre_earnings['Genre'], autopct='%.2f')
plt.title('Pie Chart: Highest Prize Earnings by Genre', size = 25)
plt.axis('equal')




#bar graph player earnings
plt.figure(figsize=(20,10)) #setting fig size to fit all the data
sns.barplot(x=top_earnings_players['Name'], y=top_earnings_players['TotalUSDPrize']) # x and y axis
plt.title('Highest Earning Players', size=25) 
plt.ylabel('Total Prize Money (USD)(Millions)', size = 20)
plt.xticks(rotation=15)
plt.xlabel('Players', size=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(['dk = Denmark', 'fi = Finland', 'au = Australia', 'fr = France', 'de = Germany', 'jo = Jordan', 'bg = Bulgaria', 'lb = Lebanon'],prop={'size': 18})
#plt.show()

df_country = df_country.rename(columns={'Two_Letter_Country_Code':'CountryCode'})
df_players['CountryCode'] = df_players['CountryCode'].apply(lambda x: x.upper()) #making all the codes upper case
df_new = pd.merge(df_players, df_country,how='left', on='CountryCode') #merging data frams on country code so it is easier to group the data

player_country = pd.DataFrame(df_new.groupby('Three_Letter_Country_Code')['PlayerId'].count().sort_values(ascending=False).reset_index()) #grouping the players by country
print(player_country)
country_geo = 'world_countries.json' #using a json file for the world map

player_map = folium.Map(location=[0, 0], zoom_start=2) #using the folium library to create a map

folium.Choropleth(geo_data = country_geo, #geography for map is my json file
                 data=player_country, #data is the players and countries they're from
                 columns=['Three_Letter_Country_Code', 'PlayerId'], #columns from the data
                 key_on='feature.id', #binds the data to a fature in my json file
                 fill_color='YlOrRd', #the colors I chose
                 fill_opacity=0.7,
                 line_opacity=0.2,
                 legend_name='Players by each Country',
                 
                 ).add_to(player_map)
player_map.save('index.html') # saving to an .html file so i can see what it looks like visually


lr = LinearRegression()

x = df_teams[['TotalTournaments']].values
y = df_teams[['TotalUSDPrize']].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .2)
lr.fit(x_train,y_train)
y_pred = lr.predict(x_test)
plt.clf()
# Plot outputs
plt.scatter(x_train, y_train, color="black")
plt.plot(x_test, y_pred, color="blue", linewidth=3)
plt.title('Expected Prize Money Based on Tournaments', size=25) 
plt.ylabel('Total Prize Money (USD)(Millions)', size = 20)
plt.xlabel('Total Tournaments', size=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)


plt.show()

print(df_new)