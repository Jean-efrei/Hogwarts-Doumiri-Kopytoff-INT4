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

    for key in character:
        value = character[key]

        if key == "Attributes":
            print(key + ":")
            for sub_key in value:
                print("- " + str(sub_key) + ": " + str(value[sub_key]))

        elif key == "Inventory" or key == "Spells":
            print(key + ":")
            if value != []:
                elements = []
                for element in value:
                    elements.append(str(element))
                print(", ".join(elements))
        else:
            print(key + ": " + str(value))


def modify_money(character, amount):
    character["Money"]=character["Money"]+amount

def add_item(character, key, item):
    if key in ["Inventory", "Spells"]:
        character[key].append(item)


if __name__ == "__main__":
    attributes = {
        "Courage": 8,
        "Intelligence": 8,
        "Loyalty": 8,
        "Ambition": 8
    }

    character = init_character("Potter", "Harry", attributes)

    display_character(character)

    modify_money(character, -20)
    add_item(character, "Inventory", "Magic Wand")
    add_item(character, "Spells", "Expelliarmus")

    print("\nAfter updates:\n")
    display_character(character)



