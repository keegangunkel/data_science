from bs4 import BeautifulSoup
from urllib.request import urlopen
import time




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
print(nameIDs_blackPantherTwo)

def imdbFetchPerson(nameID):


# https://www.imdb.com/name/nm4004793