import requests
from bs4 import BeautifulSoup
import doltcli


URL = 'https://www.fastfoodmenuprices.com/mcdonalds-nutrition/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
db = doltcli.Dolt("../../../")

menuCategories = ["burgers & sandwhiches", "wraps","chicken","salads","breakfast","sides","drinks"]

items = soup.find_all("td", class_="column-1")

def itemIsCategory(item):
    for category in menuCategories:
        item = item.lower().strip()
        if category.lower() == item:
            print(item.lower())
            return True
        else:
            continue
    return False

def getName(item):
    return item.getText().replace('\n', ' ').replace("<br/>", "")

def getNutritionalInfo(item, columnNum):
    td = ""
    # calories
    if columnNum == 1:
        td = item.nextSibling.next_element
    # fat
    if columnNum == 2: 
        td = item.nextSibling.nextSibling.next_element
    # cholesterol
    if columnNum == 3: 
        td = item.nextSibling.nextSibling.nextSibling.next_element
    # carbs
    if columnNum == 4: 
        td = item.nextSibling.nextSibling.nextSibling.nextSibling.next_element
    # fiber
    if columnNum == 5: 
        td = item.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.next_element
    # sugars
    if columnNum == 6: 
        td = item.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.next_element
    # protein
    if columnNum == 7: 
        td = item.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.next_element

    res = str(td.string)
    if res == "None":
        res = td["value"]

    return res.replace(" ", "").replace("mg", "").replace("g", "").replace(" ", "")


def buildRows():
    rows = []
    for item in items:
        name = getName(item)
        skip = itemIsCategory(name)        
        if skip == True:
            continue
        else:
            calories = getNutritionalInfo(item, 1)
            fat = getNutritionalInfo(item, 2)
            cholesterol = getNutritionalInfo(item, 3)
            carbs = getNutritionalInfo(item, 4)
            fiber = getNutritionalInfo(item, 5)
            sugar = getNutritionalInfo(item, 6)
            protein = getNutritionalInfo(item, 7)

            itemDict = {
                "name": name,
                "restaurant_name": "McDonald's",
                "identifier": "National",
                "calories": calories,
                "fat(g)": fat,
                "cholesterol(mg)": cholesterol,
                "carbohydrates": carbs,
                "fiber(g)": fiber,
                "sugars(g)": sugar,
                "protein": protein
            }
            rows.append(itemDict)
    return rows


rows = buildRows()
doltcli.write_rows(db, "menu_items", rows)
