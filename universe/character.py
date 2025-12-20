def init_character(last_name, first_name, attributes):
    character = {
        "Last Name": last_name,
        "First Name": first_name,
        "Money": 100,
        "Inventory": [],
        "Spells": [],
        "Attributes": attributes
    }
    return character


def display_character(character):
    print("Character profile:")
    for cle, val in character.items():
        print(f"{cle}:", end=" ")

        if isinstance(val, dict):
            print()
            for sub_cle, sub_val in val.items():
                print(f"  - {sub_cle}: {sub_val}")
        elif isinstance(val, list):
            if val:
                print(", ".join(map(str, val)))
            else:
                print("empty")
        else:
            print(val)


def modify_money(character, amount):
    character["Money"]=character["Money"]+amount

def add_item(character, key, item):
    if key in ["Inventory", "Spells"]:
        character[key].append(item)



