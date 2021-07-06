import requests
from bs4 import BeautifulSoup
import doltcli


URL = 'https://www.fastfoodmenuprices.com/mcdonalds-nutrition/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
db = doltcli.Dolt("../../../")

menuCategories = ["burgers & sandwhiches", "wraps","chicken","salads","breakfast","sides","drinks"]

items = soup.find_all("td", class_="column-1")
calories = soup.find_all("td", class_="column-2")
fat = soup.find_all("td", class_="column-3")
cholesterol = soup.find_all("td", class_="column-4")
carbs = soup.find_all("td", class_="column-5")
fiber = soup.find_all("td", class_="column-6")
sugars = soup.find_all("td", class_="column-7")
protein = soup.find_all("td", class_="column-8")
filteredItems = []

def itemIsCategory(item):
    for category in menuCategories:
        item = item.lower().strip()
        if category.lower() == item:
            print(item.lower())
            return True
        else:
            continue
    return False

def getCalories(item):
    calTd = item.nextSibling.string
    cal = str(calTd)
    
    # There is a small subset of td's with elements as children
    if cal == "None":
        contents = item.nextSibling.contents
        # The first child for these contents stores the calories in the 'value' attribute
        if len(contents) == 2:
            cal = contents[0]["value"]
            # The first child is a string of the calorie value
        if len(contents) == 3:
            cal = contents[0]

    # Remove any trailing spaces
    return cal.replace(" ", "")


def getName(item):
    return item.getText().replace('\n', ' ').replace("<br/>", "")

def getFatG(item):
    fatTd = item.nextSibling.nextSibling.next_element.string
    fatTdString = str(fatTd)
    fat = ""
    if fatTdString != "None":
        fat = fatTdString.replace("g", "")
    if str(fatTdString) == "None":
        fat = str(item.nextSibling.nextSibling.next_element["value"])
    return fat.replace(" ", "")

def getCholesterol(item):
    cholTd = item.nextSibling.nextSibling.nextSibling.next_element.string
    cholTdString = str(cholTd)
    cholesterol = ""
    if cholTdString != "None":
        cholesterol = cholTdString.replace("mg", "")
    if str(cholTdString) == "None":
        cholesterol = str(item.nextSibling.nextSibling.nextSibling.next_element["value"])
    return cholesterol.replace(" ", "")

def getCarbs(item):
    carbTd = item.nextSibling.nextSibling.nextSibling.nextSibling.next_element.string
    carbTdString = str(carbTd)
    carb = ""
    if carbTdString != "None":
        carb = carbTdString.replace("g", "")
    if str(carbTdString) == "None":
        carb = str(item.nextSibling.nextSibling.nextSibling.nextSibling.next_element["value"])
    return carb.replace(" ", "")

def getFiber(item):
    carbTd = item.nextSibling.nextSibling.nextSibling.nextSibling.next_sibling.next_element.string
    carbTdString = str(carbTd)
    carb = ""
    if carbTdString != "None":
        carb = carbTdString.replace("g", "")
    if str(carbTdString) == "None":
        carb = str(item.nextSibling.nextSibling.nextSibling.nextSibling.next_sibling.next_element["value"])
    return carb.replace(" ", "")

def getSugar(item):
    carbTd = item.nextSibling.nextSibling.nextSibling.nextSibling.next_sibling.next_sibling.next_element.string
    carbTdString = str(carbTd)
    carb = ""
    if carbTdString != "None":
        carb = carbTdString.replace("g", "")
    if str(carbTdString) == "None":
        carb = str(item.nextSibling.nextSibling.nextSibling.nextSibling.next_sibling.next_sibling.next_element["value"])
    return carb.replace(" ", "")

def getProtein(item):
    carbTd = item.nextSibling.nextSibling.nextSibling.nextSibling.next_sibling.next_sibling.next_sibling.next_element.string
    carbTdString = str(carbTd)
    carb = ""
    if carbTdString != "None":
        carb = carbTdString.replace("g", "")
    if str(carbTdString) == "None":
        carb = str(item.nextSibling.nextSibling.nextSibling.nextSibling.next_sibling.next_sibling.next_sibling.next_element["value"])
    return carb.replace(" ", "")


def buildRows():
    rows = []
    for item in items:
        # build cell data
        name = getName(item)
        skip = itemIsCategory(name)        
        if skip == True:
            continue
        else:
            calories = getCalories(item)
            fat = getFatG(item)
            cholesterol = getCholesterol(item)
            carbs = getCarbs(item)
            fiber = getFiber(item)
            sugar = getSugar(item)
            protein = getProtein(item)

            # skip category/header rows
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
# print(rows)

doltcli.write_rows(db, "menu_items", rows)

