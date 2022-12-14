import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import folium
from IPython.display import display


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

df_players["Name"] = df_players["NameFirst"] +" "+ df_players["NameLast"] +"("+df_players["CountryCode"]+")"

top_earnings_players = df_players.groupby(['Name'])['TotalUSDPrize'].sum().sort_values(ascending=False).reset_index()#grouping the player and earnings to graph
top_earnings_players = top_earnings_players.nlargest(10, 'TotalUSDPrize')
print(top_earnings_players)






#bar graph team earnings
plt.figure(figsize=(20,10)) #setting fig size to fit all the data
sns.barplot(x=top_earnings['Game'], y=top_earnings['TotalUSDPrize']) # x and y axis
plt.title('Highest Earning Games', size=25) 
plt.ylabel('Total Prize Money (USD)(Ten Millions)', size = 17)
plt.xticks(rotation=15)
plt.xlabel('Games', size=17)

# pie chart team earnings
plt.figure(figsize=(12,10))
plt.pie(top_earnings['TotalUSDPrize'], labels=top_earnings['Game'], autopct='%.2f')
plt.title('Pie Chart: Highest Prize Earnings by Game', size = 25)
plt.axis('equal')

#pie chart genre earnings
plt.figure(figsize=(12,10))
plt.pie(genre_earnings['TotalUSDPrize'], labels=genre_earnings['Genre'], autopct='%.2f')
plt.title('Pie Chart: Highest Prize Earnings by Genre', size = 25)
plt.axis('equal')


#bar graph player earnings
plt.figure(figsize=(20,10)) #setting fig size to fit all the data
sns.barplot(x=top_earnings_players['Name'], y=top_earnings_players['TotalUSDPrize']) # x and y axis
plt.title('Highest Earning Players', size=25) 
plt.ylabel('Total Prize Money (USD)(Millions)', size = 17)
plt.xticks(rotation=15)
plt.xlabel('Players', size=17)
plt.legend(['dk = Denmark', 'fi = Finland', 'au = Australia', 'fr = France', 'de = Germany', 'jo = Jordan', 'bg = Bulgaria', 'lb = Lebanon'])
#plt.show()

df_country = df_country.rename(columns={'Two_Letter_Country_Code':'CountryCode'})
df_players['CountryCode'] = df_players['CountryCode'].apply(lambda x: x.upper())
df_new = pd.merge(df_players, df_country,how='left', on='CountryCode')
player_country = pd.DataFrame(df_new.groupby('Country_Name')['PlayerId'].count().sort_values(ascending=False).reset_index()).head(10)

player_country_3 = pd.DataFrame(df_new.groupby('Three_Letter_Country_Code')['PlayerId'].count().sort_values(ascending=False).reset_index())

country_geo = 'world_countries.json'

player_map = folium.Map(location=[0, 0], zoom_start=2)

folium.Choropleth(geo_data = country_geo,
                 data=player_country_3,
                 columns=['Three_Letter_Country_Code', 'PlayerId'],
                 key_on='feature.id',
                 fill_color='YlOrRd',
                 fill_opacity=0.7,
                 line_opacity=0.2,
                 legend_name='Players by each Country'
                 ).add_to(player_map)
display(player_map)