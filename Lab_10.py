from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import urllib.request
import re


def imdbFetchFilm(filmID):
    """ returns list of nameID numbers like ["nm0000291", "nm3363032", ...] """

    url = "https://www.imdb.com/title/" + filmID + "/fullcredits"
    print("Fetching URL: '" + url + "'")
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    # MANDATORY DELAY TO BE POLITE
    time.sleep(1)
    
    castTable = soup.find_all("table", "cast_list")[0]
    #print(castTable)
    
    tdList = castTable.find_all("td", "primary_photo")
    #print(tdList)
    nameIDs = []
    for td in tdList:
        #print("\n" + str(td) + "\n")
        aTag = td.find_all("a")[0]
        href = aTag.get('href')
        nameID = href.strip("/").split("/")[1]
        #print(nameID)
        nameIDs.append(nameID)
    return nameIDs

nameIDs_blackPantherTwo = imdbFetchFilm("tt9114286")
print("Cast Ids: ",nameIDs_blackPantherTwo)

def imdbFetchPerson(nameID):
    url = "https://www.imdb.com/name/nm4004793"
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
    page = urllib.request.urlopen( req )
    print("Fetching URL: '" + url + "'")
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    filmIds = []
    #for film in filmList:
    for s in soup.find_all("button",id=re.compile("nm-flmg_cred-act.*-tt.*")):
        filmIds.append(s.get('id').split('-')[-1])
    return filmIds

#Letitia Wright
filmIds1 = imdbFetchPerson("nm4004793")
print("\nFilm Ids: ",filmIds1,"\n")
#Black panther 2
nameIDs1 = imdbFetchFilm("tt9114286")
print("\nCast Ids: ",nameIDs1,'\n')

## Will ferrell
filmIds2 = imdbFetchPerson("nm0002071")
print("\nFilm Ids: ",filmIds2,"\n")
### Step brothers
nameIDs2 = imdbFetchFilm("tt0838283")
print("\nCast Ids: ",nameIDs2,'\n')

## Adam Sandler
filmIds3 = imdbFetchPerson("nm0001191")
print("\nFilm Ids: ",filmIds3,"\n")
### Talladega Knights
nameIDs3 = imdbFetchFilm("tt0415306")
print("\nCast Ids: ",nameIDs3,'\n')

## Rob Schneider
filmIds2 = imdbFetchPerson("nm0001705")
print("\nFilm Ids: ",filmIds2,"\n")
### Anchorman
nameIDs2 = imdbFetchFilm("tt0357413")
print("\nCast Ids: ",nameIDs2,'\n')

## Steve Carrell
filmIds2 = imdbFetchPerson("nm0136797")
print("\nFilm Ids: ",filmIds2,"\n")
## Water Boy
nameIDs2 = imdbFetchFilm("tt0120484")
print("\nCast Ids: ",nameIDs2,'\n')


