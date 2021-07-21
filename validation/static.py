menus_primary_keys = ["name", "restaurant_name", "identifier"]
delivery_services = ["grubhub", "ubereats", "caviar", "door dash"]
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
    {"char": "  "},
    {"char": " )", "replacement": ")"},
    {"char": "( ", "replacement": "("}
]
