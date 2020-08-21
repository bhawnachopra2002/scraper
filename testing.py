import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from html.parser import HTMLParser
start=time.asctime( time.localtime(time.time()) )
li=['ART_AND_DESIGN','AUTO_AND_VEHICLES','BEAUTY','BOOKS_AND_REFERENCE','BUSINESS','COMICS',		
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
l1=['BEAUTY']
for i in li:
    url="https://play.google.com/store/apps/category/"+i
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    mylist = soup.find_all('div',class_="Vpfmgd",limit=None)
    c=len(mylist)
    linklist=[]
    applist=[]
    lf=[]
    count=0
    for j in range(c):
        link,appname,r=findit(soup,j)
        if appname in applist:
            continue
        else:
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
            print(count)
        
    for k in set(linklist):
        response = requests.get(k)
        soup = BeautifulSoup(response.text, 'html.parser')
        list1=soup.find_all('div',class_="b8cIId ReQCgd Q9MA7b")
        for j in list1:
            k=j.contents[0]
            link=k['href']
            appname=k.contents[0]['title']
            if appname not in applist:         
                response = requests.get("https://play.google.com"+link)
                soup = BeautifulSoup(response.text, 'html.parser')
                stars=soup.findAll("div",{"class": "BHMmbe"})
                try:
                    rating=stars[0].string
                except:
                    rating="No ratings"
                mylinks = soup.findAll("a", {"class": "hrTbp R8zArc"})
                genre=mylinks[1].string
                
            #     mylinks = soup.findAll("a", {"class": "hrTbp R8zArc"})
            #     genre=mylinks[1].string 
            #     try:
            #         rating=r[j].contents[0]['aria-label'][6:9]
            #     except IndexError:
            #         rating="None"
                lf.append([appname,genre,rating])
                count=count+1
                # print(appname,genre,rating)
                print(count)

    end=time.asctime( time.localtime(time.time()) )
print(len(lf))
print(start)
print(end)