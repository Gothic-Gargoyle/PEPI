# Name: EbayApiConnectionPython
# Date: 23-01-2019 12:23
# Version: 1.0
# Description: Searches a specified ebay site (de/nl/uk etc.) for a given item and returns the
# prices it sold at in the previous year(s) in graph form.
# Changelog:
# 28-06-2019: After a fair while of not doing anything, tidying up and committing again.

from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup

# Application Production ID
app_id = 'APPID'

site = input('Which ebay site would you like to search? Default = EBAY-DE (EBAY-DE, EBAY-UK, EBAY-US)\n') or 'EBAY-DE'

keywords = input('what are you searching for? (ex: white piano)\n') or "Märklin 3147"

category = input("What category would you like to look it up?") or ""

api = finding(siteid=site, appid=app_id, config_file=None)  #  <--wat is config_file?
api_request = {'keywords': keywords }
response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content,'lxml') 
totalentries = int(soup.find('totalentries').text) 
items = soup.find_all('item')

retrieved_item_list = []

for item in items:

    cat = item.categoryname.string.lower()
    title = item.title.string.lower()
    price = int(round(float(item.currentprice.string)))
    url = item.viewitemurl.string.lower()

    retrieved_item_list.append([title, price, url])

    print('________')
    print('cat:\n' + cat + '\n')
    print('title:\n' + title + '\n')
    print('price:\n' + '€' + str(price) + '\n')
    print('url:\n' + url + '\n')

print(str(len(retrieved_item_list)) + ' instances of: ' + keywords + ' have been found!')

