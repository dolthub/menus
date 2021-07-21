from static import *

def stringPassesLeadingTrailingSpaceCheck(s):
    if s == "":
        return False
    stripped = s.strip()
    return stripped == s

def stringIsUppercase(s):
    return s.upper() == s

def validateString(colName, value):
    formatted = value.strip().upper()
    for dict in invalid_chars:
        char = dict["char"]
        if char in formatted:
            if "exception" in dict and dict["exception"] in formatted: 
                continue
            else:
                formatted = formatted.replace(char, " ").replace("  ", " ").strip()
    if formatted != value:
        print(f'UPDATE menu_items SET {colName} = {formatted!r} WHERE {colName} = {value!r}')
        print(f'DELETE FROM menu_items WHERE {colName} = {value!r}')
