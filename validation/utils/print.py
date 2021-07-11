def printInvalidSpace(colName, s):
    print(f'\nmenu_item.{colName!r} "{colName!r} has leading or trailing spaces. Run the following SQL command to make corrections:\n')
    print(f'UPDATE menu_items SET {colName!r} = {s.strip()!r} WHERE restaurant_name = {s!r}')
    print(f'DELETE FROM menu_items WHERE name = {s!r}')

def printInvalidUppercase(colName, s):
    print(f'UPDATE menu_items SET {colName!r} = {s.UPPER()!r} WHERE restaurant_name = {s!r}')
    print(f'DELETE FROM menu_items WHERE {colName!r} = {s!r}')

def printInvalidChar(colName, s, char):
    print(f'UPDATE menu_items SET {colName!r} = {s.REPLACE(char, "")!r} WHERE restaurant_name = {s!r}')
    print(f'DELETE FROM menu_items WHERE {colName!r} = {s!r}')
