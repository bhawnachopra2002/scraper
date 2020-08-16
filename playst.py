import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import csv

def wricsv(a,b,c):
    with open('result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([a,b,c])
        
def findit(soup):
    mylinks = soup.findAll("a", {"class": "hrTbp R8zArc"})
    genre=mylinks[1].string
    #print(genre) #genre
    rating=soup.findAll("div",{"class": "BHMmbe"})
    star=rating[0].string
    # print(star) #rating
    appname=soup.find("h1",{"class":"AHFaub"})
    appname=appname.string
    # print(appname)   #name
    return appname,star,genre
def simapps(soup,list1,c):
    sim=soup.findAll("a", {"class": "poRVub"})
    for i in sim:
        x="https://play.google.com"+i['href']
        url=x
        response = requests.get(url)
        # print(response)
        soup = BeautifulSoup(response.text, 'html.parser')
        appname,star,genre=findit(soup)
        if appname not in list1:
            list1.append(appname)
            c=c+1
        else:
            # print("repeated")
            i=1
            while(appname in list1 and i<len(sim)):
                x="https://play.google.com"+sim[i]['href']
                url=x
                response = requests.get(url)
                # print(response)
                soup = BeautifulSoup(response.text, 'html.parser')
                appname,star,genre=findit(soup)
                i=i+1
            list1.append(appname)
            c=c+1
        wricsv(appname,genre,star)
        if c%10:
            print(c)
    if c<1000:
        simapps(soup,list1,c)
    
url='https://play.google.com/store/apps/details?id=com.amazon.sellermobile.android'
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.text, 'html.parser')
list1=[]
appname,star,genre=findit(soup)
list1.append(appname)
c=1
with open('result.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["appname","genre","ratings"])
wricsv(appname,genre,star)
simapps(soup,list1,c)

