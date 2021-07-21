menus_primary_keys = ["name", "restaurant_name", "identifier"]

invalid_chars = [
    {"char": "®"},
    {"char": "™"},
    {"char": "©"},
    {"char": "℠"},
    {"char": "*"},
    {"char": '"'},
    {"char": "''"},
    {"char": " 'S", "exception": "'SHROOM"},
    {"char": " ' "},
    {"char": "  "}
]
