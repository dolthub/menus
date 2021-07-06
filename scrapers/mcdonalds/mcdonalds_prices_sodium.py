import requests
from bs4 import BeautifulSoup
import doltcli

URL = "http://www.fastfoodwatch.com/mcdonalds-menu-prices/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
db = doltcli.Dolt("../../../")

tableRows = soup.find_all("tr")

def scrapePricesAndSodium():
    res = []
    for r in tableRows:
        tds = r.find_all("td")
        name = ""
        price = ""
        sodium = ""
        if len(tds) > 2:
            name = tds[0].getText()
            price = tds[1].getText()
            if len(tds) > 5:
                sodium = tds[6].getText()

            query = "SELECT * FROM menu_items WHERE name LIKE '%" + name  + "%' ORDER BY LENGTH(name) ASC"
            readRows = doltcli.read_rows_sql(db, query)
            for rows in readRows:
                if len(rows) > 1:
                    if str("Big Breakfast with Hotcakes") in rows["name"]:
                        rows["price(usd)"] = "5.29"
                        rows["sodium(mg)"] = "2150"
                        break
                    elif rows["name"] == str("Big Breakfast"):
                        rows["price(usd)"] = "3.49"
                        rows["sodium(mg)"] = "1560"
                    elif rows["name"] == str("Hotcakes"):
                        rows["price(usd)"] = "2.29"
                        rows["sodium(mg)"] = "590"
                    elif rows["name"] == str("McChicken ®"):
                        rows["price(usd)"] = "1.00"
                        rows["sodium(mg)"] = "650"
                    else:
                        rows["price(usd)"] = price.replace("$", "").replace(" ", "").replace("\xa0", "")
                        rows["sodium(mg)"] = sodium.replace("mg", "").replace(" ", "").replace("\xa0", "")
                        res.append(rows)
    return res

rowsWithPrice = scrapePricesAndSodium()
doltcli.write_rows(db, "menu_items", rowsWithPrice, "update")
