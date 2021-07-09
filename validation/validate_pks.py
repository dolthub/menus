from utils.strings import *
from utils.print import *
from static import *


def validateName(name):
  if len(name) < 3:
    msg = f"\nmenu_item.name {name!r} has less than 3 characters. Is that correct?"
    print(msg)


def validateRestaurantName(restaurant_name):
  if len(restaurant_name) < 3:
    print(f'menu_item.restaurant_name {restaurant_name!r} has less than 3 characters. Is that correct?')


def validateIdentifier(identifier):
  if identifier == "NATIONAL":
    return
  if "," not in identifier:
    print(f'\nmenu_item.identifier "{identifier!r} must be equal to "NATIONAL", or in the format of <city>, <state>.\nExample: Santa Monica, CA\nIf the menu items are statewide, use NULL, <state>')

def validatePkIsUppercase(colName, value):
  if stringIsUppercase(value) is False:
    printUppercaseCorrectionPrompt(colName, value)
  
def validatePkHasNoLeadingTrailingSpaces(colName, value):
    if stringPassesLeadingTrailingSpaceCheck(value) is not True:
      printLeadingTrailingSpaceCorrectionPrompt(colName, value)
    if stringIsUppercase(value) is not True:
      printUppercaseCorrectionPrompt(colName, value)

def validateNoInvalidChars(colName, value):
  for char in invalid_chars:
    if char in value:
      printInvalidCharCorrectionPrompt(colName, value, char)


def validateCommonPkFormat(row):
  for pk in menus_primary_keys:
    validatePkIsUppercase(pk, row[pk])
    validatePkHasNoLeadingTrailingSpaces(pk, row[pk])
    validateNoInvalidChars(pk, row[pk])


def validatePks(row):
    validateCommonPkFormat(row)

    # Tests specific formatting for the column
    validateName(row["name"])
    validateRestaurantName(row["restaurant_name"])
    validateIdentifier(row["identifier"])

    