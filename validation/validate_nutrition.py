
import doltcli

nutrition_fields = ["calories", "fat_g", "carbohydrates_g", "protein_g", "sodium_mg", "price_usd","cholesterol_mg", "fiber_g", "sugars_g" ]

def validateNoUnitsInCells(db, row):
    for field in nutrition_fields:
        fieldName = (f'{field!r}').replace("'", "")
        value = row[fieldName]
        stripped = value.replace("mg", "").replace("g", "").replace("(", "").replace(")","").strip()
        if stripped != value:
            doltcli.write_rows(db, "menu_items", [row], "update")
            db.sql(f"DELETE FROM menu_items WHERE name = {value!r}")
            print(f'\nmenu_item.{field!r} "{value!r} was stripped of leading or trailing spaces, units, and or parentheses. Please commit these changes.')
