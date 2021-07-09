def validateName(name):
  if len(name) < 3:
    msg = f"\nmenu_item.name {name!r} has less than 3 characters. Is that correct?"
    print(msg)

  stripped = name.strip()
  if stripped != name:
    print(f'\nmenu_item.name "{name!r} has leading or trailing spaces.')
    print("Run the following SQL command to make corrections:")
    print(f'\nUPDATE menu_items SET name = {stripped!r} WHERE name = {name!r}')
    print(f'DELETE FROM menu_items WHERE name = {name!r}\n')


def validateRestaurantName(name):
  if len(name) < 3:
    print(f'menu_item.restaurant_name {name!r} has less than 3 characters. Is that correct?')

  stripped = name.strip()
  if stripped != name:
    print(f'menu_item.restaurant_name "{name!r} has leading or trailing spaces. Run the following SQL command to make corrections:\n')
    print(f'UPDATE menu_items SET restaurant_name = {stripped!r} WHERE restaurant_name = {name!r}')
    print(f'DELETE FROM menu_items WHERE name = {name!r}')


def validateIdentifier(identifier):
  if identifier == "NATIONAL":
    return
  if "," not in identifier:
    print(f'\nmenu_item.identifier "{identifier!r} must be equal to "NATIONAL", or in the format of <city>, <state>.\nExample: Santa Monica, CA\nIf the menu items are statewide, use NULL, <state>')
  stripped = identifier.strip()
  if stripped != identifier:
    print(f'\nmenu_item.identifier "{identifier!r} has leading or trailing spaces. Run the following SQL command to make corrections:\n')
    print(f'UPDATE menu_items SET restaurant_name = {stripped!r} WHERE restaurant_name = {identifier!r}')
    print(f'DELETE FROM menu_items WHERE name = {identifier!r}')

def validatePks(row):
    validateName(row["name"])
    validateRestaurantName(row["restaurant_name"])
    validateIdentifier(row["identifier"])

    