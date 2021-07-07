
from validate_nutrition import *
import doltcli
from validate_pks import *

relative_path_to_dolt_directory = "FILL ME IN"
db = doltcli.Dolt(relative_path_to_dolt_directory)

def validatePks(row):
    validateName(row["name"])
    validateRestaurantName(row["restaurant_name"])
    validateIdentifier(row["identifier"])


def main():
  rows = doltcli.read_rows_sql(db, "SELECT * FROM menu_items")
  for row in rows:
    validatePks(row)
    validateNoUnitsInCells(db, row)

main()