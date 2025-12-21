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
        val = character[key]
        print(str(key) + ":", end=" ")

        if type(val) == dict:
            print()
            for sub_key in val:
                sub_val = val[sub_key]
                print("  - " + str(sub_key) + ": " + str(sub_val))

        elif type(val) == list:
            if val == []:
                print("empty")
            else:
                elements_str = []
                for element in val:
                    elements_str.append(str(element))
                for i in range(len(elements_str)):
                    if i < len(elements_str) - 1:
                        print(elements_str[i] + ",", end=" ")
                    else:
                        print(elements_str[i])

        else:
            print(val)


def modify_money(character, amount):
    character["Money"]=character["Money"]+amount

def add_item(character, key, item):
    if key in ["Inventory", "Spells"]:
        character[key].append(item)



