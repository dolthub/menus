import requests
from bs4 import BeautifulSoup
import doltcli

URL = "http://www.fastfoodwatch.com/mcdonalds-menu-prices/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
db = doltcli.Dolt("../../../")

tableRows = soup.find_all("tr")
res = []

for r in tableRows:
    tds = r.find_all("td")
    name = ""
    price = ""
    if len(tds) > 2:
        name = tds[0].getText()
        price = tds[1].getText()
        itemPriceDict = {
            "name": name,
            "restaurant_name": "McDonald's",
            "identifier": "National",
            "price(usd)": price.replace("$", "").replace(" ", "").replace("\xa0", ""),
        }
        query = "SELECT * FROM menu_items WHERE name LIKE '%" + name  + "%'"
        readRows = doltcli.read_rows_sql(db, query)
        for rows in readRows:
            rows["price(usd)"] = price.replace("$", "").replace(" ", "").replace("\xa0", "")
            res.append(rows)

print(res, "\n")
doltcli.write_rows(db, "menu_items", res, "update")