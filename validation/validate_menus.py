
from os import error
import doltcli


URL = 'https://en.wikipedia.org/wiki/List_of_restaurant_chains_in_the_United_States'
db = doltcli.Dolt("../../../")

def validateName(db, row):
  name = row["name"]
  if len(name) < 3:
    print(f'menu_item.name {name!r} has less than 3 characters. Is that correct?')

  stripped = name.strip()
  if stripped != name:
    row["name"] = stripped
    doltcli.write_rows(db, "menu_items", [row], "update")
    print(f'menu_item.name "{name!r} was stripped of leading or trailing spaces. Please commit these changes.')

def validateRestaurantName(db, row):
  name = row["restaurant_name"]
  if len(name) < 3:
    print(f'menu_item.restaurant_name {name!r} has less than 3 characters. Is that correct?')

  stripped = name.strip()
  if stripped != name:
    row["restaurant_name"] = stripped
    doltcli.write_rows(db, "menu_items", [row])
    print(f'menu_item.restaurant_name "{name!r} was stripped of leading or trailing spaces. Please commit these changes.')

def validateIdentifier(identifier):
  if identifier == "National":
    return
  if "," not in identifier:
    print(f'menu_item.identifier "{identifier!r} must be equal to "National", or in the format of <city>, <state>.\nExample: Santa Monica, CA\nIf the menu items are statewide, use NULL, <state>')

  

def main():
  rows = doltcli.read_rows_sql(db, "SELECT * FROM menu_items")
  for row in rows:
    validateName(db, row)
    validateRestaurantName(db, row)
    validateIdentifier(row["identifier"])

main()