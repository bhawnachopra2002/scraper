import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool
start_time=time.time()
categorylist=['ART_AND_DESIGN','AUTO_AND_VEHICLES','BEAUTY','BOOKS_AND_REFERENCE','BUSINESS','COMICS',		
'COMMUNICATION',	
'DATING','EDUCATION',		
'ENTERTAINMENT',	
'EVENTS',		
'FINANCE',		
'FOOD_AND_DRINK',		
'HEALTH_AND_FITNESS',		
'HOUSE_AND_HOME',		
'LIFESTYLE',		
'MAPS_AND_NAVIGATION',		
'MEDICAL',	
'MUSIC_AND_AUDIO',	
'NEWS_AND_MAGAZINES',		
'PARENTING',		
'PERSONALIZATION',		
'PHOTOGRAPHY',		
'PRODUCTIVITY',
'SHOPPING',		
'SOCIAL',		
'SPORTS',		
'TOOLS',
'TRAVEL_AND_LOCAL',		
'VIDEO_PLAYERS',		
'WEATHER',		
'LIBRARIES_AND_DEMO',
'GAME_ARCADE',		
'GAME_PUZZLE',		
'GAME_CARD',		
'GAME_CASUAL',		
'GAME_RACING',		
'GAME_SPORTS',	
'GAME_ACTION',		
'GAME_ADVENTURE',
'GAME_BOARD',		
'GAME_CASINO',		
'GAME_EDUCATIONAL',	
'GAME_MUSIC',		
'GAME_ROLE_PLAYING',
'GAME_SIMULATION',	
'GAME_STRATEGY',
'GAME_TRIVIA',
'GAME_WORD',		
'ANDROID_WEAR']	
def findit(soup,j):
    a1=soup.findAll("a", {"class": "poRVub"})
    link="https://play.google.com"+a1[j]['href']
    app1=soup.find_all('div',{"class":"WsMG1c nnK0zc"})
    appname=app1[j].string
    r=soup.find_all('div',class_="pf5lIe")
    return link,appname,r

linklist=[] # app urls
applist=[] # app names
lf=[] 
count=0  # app details
l1=["COMMUNICATION"]
for i in categorylist:
    url="https://play.google.com/store/apps/category/"+i
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    mylist = soup.find_all('div',class_="W9yFB",limit=None)
    for j in mylist:
        link="https://play.google.com"+j.contents[0]['href']
        # print(j.contents[0]['href'])
        # print(link)
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'lxml')
        mylist1 = soup.find_all('div',class_="Vpfmgd",limit=None) #list of apps on page of category
        c=len(mylist1)
        print(c)
        for j in range(c):
            link,appname,r=findit(soup,j)
            if appname not in applist:
                applist.append(appname)
                linklist.append(link)
                genre=i
                try:
                    rating=r[j].contents[0]['aria-label'][6:9]
                except IndexError:
                    rating="None"  
                lf.append([appname,genre,rating])
                count=count+1    
                # print(appname,genre,rating)
            else:
                continue
        print(len(lf))
print("--- %s seconds ---" % (time.time() - start_time))
