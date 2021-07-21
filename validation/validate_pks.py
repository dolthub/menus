from utils.strings import *
from static import *


def validateName(name):
  if len(name) < 3:
    msg = f"\nmenu_items.name {name!r} has less than 3 characters. Is that correct?"
    print(msg)

def validateRestaurantName(restaurant_name):
  if len(restaurant_name) < 3:
    print(f'menu_items.restaurant_name {restaurant_name!r} has less than 3 characters. Is that correct?')

def getStateAndServiceFromIdentifier(identifier):
  components = identifier.split(",")
  if len(components) == 2:
    state = components[1]
  if len(components) == 3:
    state = components[2]
    deliveryService = components[0]

  state = state.strip()
  deliveryService = deliveryService.strip()
  return state, deliveryService


def validateIdentifier(identifier):
  if identifier == "NATIONAL":
    return
  if "," not in identifier:
    print(f'\nmenu_items.identifier "{identifier!r} must be equal to "NATIONAL", or in the format of <city>, <state>.\nExample: Santa Monica, CA\nIf the menu items are statewide, use NULL, <state>')
  
  state, deliveryService = getStateAndServiceFromIdentifier(identifier)
  
  if len(state) != 2:
    print(f"State postal code is not in expected format: {state}")

  if deliveryService.lower() not in delivery_services:
    print(f"Unknown delivery service in identifier: {deliveryService!r}")

  

def validatePks(row):
    for pk in menus_primary_keys:
      validateString(pk, row[pk])

    # Tests specific formatting for the column
    validateName(row["name"])
    validateRestaurantName(row["restaurant_name"])
    validateIdentifier(row["identifier"])

    