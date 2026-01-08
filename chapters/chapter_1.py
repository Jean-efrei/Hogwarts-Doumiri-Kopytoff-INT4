import json
from utils.input_utils import ask_text, ask_number, ask_choice, load_file
from universe.character import init_character, display_character, modify_money, add_item




def introduction():
    print("Welcome to the magical world of Hogwarts!")
    print("Your adventure is about to begin...")
    print("You are about to receive a mysterious letter that will change your life.")
    input("\nPress Enter to continue...")


def create_character():
    last_name = ask_text("Enter your character's last name: ")
    first_name = ask_text("Enter your character's first name: ")

    print("Choose your attributes:")

    courage = ask_number("Courage level (1-10): ", 1, 10)
    intelligence = ask_number("Intelligence level (1-10): ", 1, 10)
    loyalty = ask_number("Loyalty level (1-10): ", 1, 10)
    ambition = ask_number("Ambition level (1-10): ", 1, 10)

    attributes = {
        "Courage": courage,
        "Intelligence": intelligence,
        "Loyalty": loyalty,
        "Ambition": ambition
    }

    character = init_character(last_name, first_name, attributes)
    print("\nCharacter profile:")
    display_character(character)
    return character
if __name__ == "__main__":
    introduction()
    hero = create_character()

def receive_letter():

    print("An owl flies through the window, delivering a letter sealed with the Hogwarts crest...")
    print("“Dear Student,")
    print("We are pleased to inform you that you have been accepted to Hogwarts")
    print("School of Witchcraft and Wizardry!”\n")

    choice = ask_choice("Do you accept this invitation and go to Hogwarts?",["Yes, of course!", "No, I'd rather stay with Uncle Vernon..."])

    if choice == "No, I'd rather stay with Uncle Vernon...":
        print("You tear up the letter, and Uncle Vernon cheers:")
        print("“EXCELLENT! Finally, someone NORMAL in this house!”")
        print("The magical world will never know you existed... Game over.")
        return
    print("\nYou clutch the letter tightly. Your life will never be the same again...")


def meet_hagrid(character) :
    print("Hagrid: Hello Harry! I’m here to help you with your shopping on Diagon Alley.")
    print("Do you want to follow Hagrid?")
    print("1 : yes")
    print("2 : no")
    x = ask_choice("Your choice:", ["1", "2"])
    if x == "1":
        print("Hagrid smiles : Well, follow me, ", character["First Name"])
    else:
        print("Hagrid stops : I'm sorry... but I have to insist, after you")

def buy_supplies(character):
    inventory_data = load_file("data/inventory.json")

    required_items = ["Magic Wand", "Wizard Robe", "Potions Book"]

    print("Catalog of available items:")

    item_names = []
    i = 1
    while i <= len(inventory_data):
        tmp = i
        key = ""
        if tmp == 0:
            key = "0"
        while tmp > 0:
            digit = tmp % 10
            key = chr(ord('0') + digit) + key
            tmp = tmp // 10

        name = inventory_data[key][0]
        price = inventory_data[key][1]

        print(i, ".", name, "-", price, "Galleons", end="")
        if name in required_items:
            print(" (required)")
        else:
            print()

        item_names.append(name)
        i = i + 1

    while required_items != []:
        print("You have", character["Money"], "Galleons.")
        print("Remaining required items:", ", ".join(required_items))

        choice = ask_number("Enter the number of the item to buy: ", 1, len(item_names))
        chosen_item = item_names[choice - 1]

        if chosen_item in character["Inventory"]:
            print("You already bought:", chosen_item)
        else:
            tmp = choice
            key = ""
            if tmp == 0:
                key = "0"
            while tmp > 0:
                digit = tmp % 10
                key = chr(ord('0') + digit) + key
                tmp = tmp // 10

            price = inventory_data[key][1]

            if character["Money"] < price:
                print("You do not have enough money. Game over.")
                return

            modify_money(character, -price)
            add_item(character, "Inventory", chosen_item)

            print("You bought:", chosen_item, "(-", price, "Galleons).")

            if chosen_item in required_items:
                required_items.remove(chosen_item)

    print("All required items have been purchased!")
    print("It's time to choose your Hogwarts pet!")

    pets = [("Owl", 20), ("Cat", 15), ("Rat", 10), ("Toad", 5)]

    print("You have", character["Money"], "Galleons.")
    print("Available pets:")
    i = 1
    while i <= len(pets):
        print(i, ".", pets[i - 1][0], "-", pets[i - 1][1], "Galleons")
        i = i + 1

    print("Which pet do you want?")
    i = 1
    while i <= len(pets):
        print(i, ".", pets[i - 1][0])
        i = i + 1

    pet_choice = ask_number("Your choice: ", 1, len(pets))
    pet_name = pets[pet_choice - 1][0]
    pet_price = pets[pet_choice - 1][1]

    if character["Money"] < pet_price:
        print("You do not have enough money to buy this pet. Game over.")
        return

    modify_money(character, -pet_price)
    add_item(character, "Inventory", pet_name)

    print("You chose:", pet_name, "(-", pet_price, "Galleons).")
    print("All required items have been successfully purchased! Here is your")
    print("final inventory:")
    display_character(character)

def start_chapter_1():
    introduction()
    character = create_character()
    receive_letter()
    meet_hagrid(character)
    buy_supplies(character)

    print("End of Chapter 1! Your adventure begins at Hogwarts...")
    return character

