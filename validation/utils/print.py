def printLeadingTrailingSpaceMsg(colName, s):
    print(f'\nmenu_item.{colName!r} "{colName!r} has leading or trailing spaces. Run the following SQL command to make corrections:\n')
    print(f'UPDATE menu_items SET {colName!r} = {s.strip()!r} WHERE restaurant_name = {s!r}')
    print(f'DELETE FROM menu_items WHERE name = {s!r}')

def printUppercaseCorrectionPrompt(colName, s):
    print(f'UPDATE menu_items SET {colName!r} = {s.UPPER()!r} WHERE restaurant_name = {s!r}')
    print(f'DELETE FROM menu_items WHERE {colName!r} = {s!r}')
