dico={"Last Name":"","First Name":"","Middle Name": "","Money":"","Inventory":"","Spells":"","Attributes":""}

last_name= dico["Last Name"]
first_name = dico["First Name"]
middle_name = dico["Middle Name"]
money = dico["Money"]
inventory = dico["Inventory"]
spells = dico["Spells"]
attributes = dico["Attributes"]


def display_character():
    print(dico)
    print(last_name)
    print(first_name)
    print(middle_name)
    print(money)
    print(inventory)
    print(spells)
    print(attributes)

def modify_money(character, amount):
    character["Money"]=character["Money"]+amount

def add_item(character, key, item):
    character[key]=item
    for char in character:
        item.append(character[char])



