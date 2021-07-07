
from validate_nutrition import validateNoUnitsInCells
import doltcli
from validate_pks import *

db = doltcli.Dolt("../../../")

def validatePks(db, row):
    validateName(db, row)
    validateRestaurantName(db, row)
    validateIdentifier(row["identifier"])


def main():
  rows = doltcli.read_rows_sql(db, "SELECT * FROM menu_items")
  for row in rows:
    validatePks(db, row)
    validateNoUnitsInCells(db, row)

main()