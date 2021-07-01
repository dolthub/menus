import csv
import requests
from bs4 import BeautifulSoup
import doltcli


URL = 'https://www.fastfoodmenuprices.com/mcdonalds-nutrition/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
db = doltcli.Dolt("../../../")

menuCategories = ["burgers", "sandwhiches", "wraps","chicken","salads","breakfast","sides","drinks"]

items = soup.find_all("td", class_="column-1")
filteredItems = []
# for item in items:

def itemIsCategory(item):
    for category in menuCategories:
        # print(item.lower(), category.lower())
        if category.lower() in item.lower() or item.lower == category.lower() :
            return True
        else:
            continue


itemsForImport = []

for item in items:
    text = item.getText()
    formattedText = text.replace('\n', ' ').replace("<br/>", "")
    skip = itemIsCategory(formattedText)
    if skip == True:
        continue
    else:
        itemDict = {"name": formattedText, "restaurant_name": "McDonald's", "identifier": "National"}
        itemsForImport.append(itemDict)
        # print(formattedText)

doltcli.write_rows(db, "menu_items", itemsForImport)
