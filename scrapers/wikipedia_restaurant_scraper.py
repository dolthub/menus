import csv
import requests
from bs4 import BeautifulSoup
import doltcli


URL = 'https://en.wikipedia.org/wiki/List_of_restaurant_chains_in_the_United_States'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
db = doltcli.Dolt(".")

tables = soup.find_all("table", class_="wikitable")
rows = soup.select("table.wikitable tbody tr td:first-of-type")
with open("restaurants.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\n')
    writer.writerow(["id", "name", "type"])
    for row in rows:
        text = row.get_text()
        if "Cajun" in text and "Chinese" in text:
            break
        if "," in text or text == "edit" or "List" in text or "restaurants" in text or "chains" in text:
            continue
        else:
            name = text[0:len(text)-1]
            name = name.replace("\n", "")
            if "Old Country Buffet" in name:
                writer.writerow(["", "Old Country Buffet", ""])
            if "HomeTown Buffet" in name:
                writer.writerow(["", "HomeTown Buffet", ""])
            if "Ryan Buffet" in name:
                writer.writerow(["", "Ryan Buffet", ""])
            if "Ponderosa" in name:
                writer.writerow(["", "Ponderosa", ""])
            if "Bonanza Steakhouses" in name:
                writer.writerow(["", "Bonanza Steakhouses", ""])
            if "Checkers" in name or "Rally" in name:
                writer.writerow(["", "Checkers", ""])
                writer.writerow(["", "Rally's", ""])
            if "Carl's Jr." in name and "Hardee's" in name:
                writer.writerow(["", "Carl's Jr.", ""])
                writer.writerow(["", "Hardee's", ""])
            else:
                row = ["", name, ""]
                writer.writerow(row)
                query = "INSERT INTO `restaurants`(`id`, `name`, `type`) VALUES(,'" + text[:len(text)-1] + "',NULL);"
                print(query)
                # db.sql(query, result_format="json")


# db.table_import("restaurants", "restaurants.csv", False, True, False, None, ["id"], False, "csv", False)