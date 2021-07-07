
import doltcli

bad_chars = ["™", "--", "®"]

def validateName(db, row):
  name = row["name"]
  if len(name) < 3:
    print(f'\nmenu_item.name {name!r} has less than 3 characters. Is that correct?')

  stripped = name.strip()
  if stripped != name:
    row["name"] = stripped
    doltcli.write_rows(db, "menu_items", [row], "update")
    db.sql(f"DELETE FROM menu_items WHERE name = {name!r}", result_format="csv")
    print(f'\nmenu_item.name "{name!r} was stripped of leading or trailing spaces. Please commit these changes.')

def validateRestaurantName(db, row):
  name = row["restaurant_name"]
  if len(name) < 3:
    print(f'\nmenu_item.restaurant_name {name!r} has less than 3 characters. Is that correct?')

  stripped = name.strip()
  if stripped != name:
    row["restaurant_name"] = stripped
    doltcli.write_rows(db, "menu_items", [row])
    print(f'\nmenu_item.restaurant_name "{name!r} was stripped of leading or trailing spaces. Please commit these changes.')

def validateIdentifier(identifier):
  if identifier == "National":
    return
  if "," not in identifier:
    print(f'\nmenu_item.identifier "{identifier!r} must be equal to "National", or in the format of <city>, <state>.\nExample: Santa Monica, CA\nIf the menu items are statewide, use NULL, <state>')

