#Name: EbayApiConnectionPython
#Date: 23-01-2019 12:23
#Version: 1.0
#Description: Searches a specified ebay site (de/nl/uk etc.) for a given item and returns the
#prices it sold at in the previous year(s) in graph form.

from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup

#Application ID
app_id = '<Insert app id here>'

#zet site & keywords
site = input('Which ebay site would you like to search? (EBAY-DE, EBAY-UK, EBAY-USA)\n')

keywords = input('what are you searching for? (ex: white piano)\n')

    #maakt lijst van categorieen die bij het keyword horen

    #Selecteer categorieen

#haal daarna dingen op

api = finding(siteid= site, appid= app_id, config_file=None)#<--wat is config_file?
api_request = { 'keywords': keywords } 
response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content,'lxml') 
totalentries = int(soup.find('totalentries').text) 
items = soup.find_all('item')

#Initieert teller voor aantal gevonden items.
amount_of_items = 0

#Haalt items op en displayed ze.
for item in items:
    cat = item.categoryname.string.lower()
    title = item.title.string.lower()
    price = int(round(float(item.currentprice.string)))
    url = item.viewitemurl.string.lower()
    print('________')
    print('cat:\n' + cat + '\n')
    print('title:\n' + title + '\n')
    print('price:\n' + '€' + str(price) + '\n')
    print('url:\n' + url + '\n')
    amount_of_items += 1

#print aantal gevonden objecten    
print(str(amount_of_items) + ' instances of: ' + keywords + ' have been found!')


#Schrijf prijs + datum verkocht artikel weg in een database, met ebay ID als UID
# ID, Zoekwoord, categorie, naam, prijs, datum, ebay ID 


#maak grafiek van Y prijs X datum


#schaal grafiek per dag/week/maand/jaar
