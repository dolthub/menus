
from validate_nutrition import *
import doltcli
from validate_pks import *

relative_path_to_dolt_directory = "../../../menus/menus"
db = doltcli.Dolt(relative_path_to_dolt_directory)

def main():
  rows = doltcli.read_rows_sql(db, "SELECT * FROM menu_items")
  for row in rows:
    validatePks(row)
    validateNutrition(row)

main()