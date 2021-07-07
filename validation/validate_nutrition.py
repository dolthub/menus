
import doltcli

nutrition_fields = ["calories", "fat(g)", "carbohydrates(g)", "protein(g)", "sodium(mg)", "price(usd)","cholesterol(mg)", "fiber(g)", "sugars(g)" ]

def validateNoUnitsInCells(db, row):
    for field in nutrition_fields:
        fieldName = (f'{field!r}').replace("'", "")
        value = row[fieldName]
        stripped = value.replace("mg", "").replace("g", "").replace("(", "").replace(")","").strip()
        if stripped != value:
            doltcli.write_rows(db, "menu_items", [row], "update")
            db.sql(f"DELETE FROM menu_items WHERE name = {name!r}")
            print(f'\nmenu_item.{field!r} "{value!r} was stripped of leading or trailing spaces, units, and or parentheses. Please commit these changes.')


