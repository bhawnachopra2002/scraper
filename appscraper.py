'''first the get request for each category page is sent and then the apps in the page of see more button are scraped for each category.
After scraping all apps BFS graph theory technique is used to scrape similar apps'''
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
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
#function to return url ,appname and app ratings.
def findit(soup,j):
    a1=soup.findAll("a", {"class": "poRVub"}) #list of url of the app page
    link="https://play.google.com"+a1[j]['href']
    app1=soup.find_all('div',{"class":"WsMG1c nnK0zc"}) #list of div classes having appname
    appname=app1[j].string
    r=soup.find_all('div',class_="pf5lIe") #list of the app ratings
    return link,appname,r

linklist=[] # app urls
applist=[] # app names
lf=[] #final list to store app details.
count=0  # app details
l1=["COMMUNICATION"]
for i in categorylist:
    url="https://play.google.com/store/apps/category/"+i #To browse first page of each category. 
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    mylist = soup.find_all('div',class_="W9yFB",limit=None) #the urls of the pages when we click see more button on category page.
    for m in mylist:
        link="https://play.google.com"+m.contents[0]['href']
        # print(link)
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'lxml')
        mylist1 = soup.find_all('div',class_="Vpfmgd",limit=None) #list of apps on collection page of each category
        c=len(mylist1)
        print(c)
        for j in range(c):
            link,appname,r=findit(soup,j)
            if appname not in applist: 
                applist.append(appname) #appending appname of unique apps to applist
                linklist.append(link) #appending appurls to link list
                genre=i #category wise sorting
                try:
                    rating=r[j].contents[0]['aria-label'][6:9]
                except IndexError:
                    rating="None"  #because for some paid apps there is no rating.
                lf.append([appname,genre,rating])
                count=count+1    
                # print(appname,genre,rating)
            else:
                continue
                
print(len(lf))
for k in linklist:
    response = requests.get(k)
    soup = BeautifulSoup(response.text, 'html.parser')
    list_sim=soup.find_all('div',class_="b8cIId ReQCgd Q9MA7b") #div containing similar apps
    for j in list_sim:
        k=j.contents[0]
        link=k['href']  #url of similar app
        appname=k.contents[0]['title']
        if appname not in applist:         
            response = requests.get("https://play.google.com"+link)
            soup = BeautifulSoup(response.text, 'lxml')
            stars=soup.findAll("div",{"class": "BHMmbe"}) #div containing rating
            try:
                rating=stars[0].string
            except:
                rating="No ratings"
            mylinks = soup.findAll("a", {"class": "hrTbp R8zArc"}) #div containg genre
            try:
                genre=mylinks[1].string
            except:
                genre="No genre"
            lf.append([appname,genre,rating]) #appending etails of each similar app to final list.
            # print(appname,genre,rating)
            count=count+1
    if count>100000: #max no of apps to be scraped
        break
print(len(lf))
#print(lf[:])
print("--- %s seconds ---" % (time.time() - start_time))
