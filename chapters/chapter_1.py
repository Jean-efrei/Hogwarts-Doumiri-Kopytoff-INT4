from utils.input_utils import *
from universe.character import init_character, display_character, modify_money, add_item
import json



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


def receive_letter(character):
    print("An owl flies through the window, delivering a letter sealed with the Hogwarts crest...")
    print("Dear Mr Potter, "
          "We are pleased to inform you that you have been accepted at Hogwarts School of Witchcraft and Wizardry."
          "Please find enclosed a list of all necessary books and equipment."
          "Term begins on 1 September. We await your owl by no later than 31 July."
          "Yours sincerely,"
          "Minerva McGonagall")
    print("Do you accept this invitation and go to Hogwarts ?")
    print("1 : Yes of course")
    print("2 : No, what is that weird letter, Wizards don't exist")
    x = ask_choice("Your choice:", ["1", "2"])
    if x == "1":
        print("A strange feeling browses your entire body, it's the beginning of a great adventure. ")
    else:
        print(
            "You tear up your letter, and throw it into the fire place, Uncle Vernon cheers : Finally someone normal in this house !")
        print("The magical world will never hear about, what a waste of magic ! GAME OVER")
        exit()


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
    inventory = load_file("data/inventory.json")
    required_items = ["Magic Wand", "Wizard Robe", "Potions Book"]
    print("Welcome to the Diagon Alley!\n")
    print("Catalog of available items : ")
    for key,value in inventory.items():
        label = "(required)" if value[0] else ""
        print("{}. {} - {} Galleons {}".format(key, value[0], value[1], label))

    while character["Money"] > 0 and required_items != []:
        print("You have ", character["Money"], "Galleons.")
        print("Remaining required items: ", end=' ')
        for item in required_items:
            if required_items.index(item) < len(required_items)-1:
                print(item, end=', ')
            else :
                print(item)

        choice = (ask_text("Which item do you want to buy?" ))
        if inventory[choice][1] > character["Money"] and inventory[choice][0] in required_items:
            print("You don't have enough money to buy the required item, GAME OVER")
            exit()
        elif inventory[choice][0] in required_items :
            required_items.remove(inventory[choice][0])

        print("You bought: ", choice, "( - ", character[choice][1], ").")
        modify_money(character, -character[choice][1])
        add_item(character, "inventory", inventory[choice][0])

    print("All required items have been purchased!")
    print("It's time to choose your Hogwarts pet!")
    print("You have ", character["Money"], "Galleons.")
    print("Available pets:")
    pets = ["Owl", "Cat", "Rat", "Toad"]
    prices = [20, 15, 10, 5]
    for pet in range(len(pets)):
        print(f"{pet + 1}, {pets[pet]} - {prices[pet]} Galleons")
        pet_choice = ask_choice("which pet do you want to buy?", pets)
        if prices[pet] > character["Money"] :
            print("You don't have enough money to buy a pet, GAME OVER")
            exit()
    modify_money(character, prices[pet])
    add_item(character, "inventory", pets[pet_choice])
    print(f"You chose : {pets[pet_choice]} (-{prices[pet_choice]})")
    print("All required items have been successfully purchased! Here is your final inventory")
    print("")
    inventory = ", ".join(character["Inventory"])
    print(inventory)
    print("Your character profile:")
    display_character(character)
    return character

def start_chapter_1():
    introduction()
    character = create_character()
    receive_letter(character)
    meet_hagrid(character)
    buy_supplies(character)
    print("This is the end of the chapter 1, your adventure in Hogwarts is about to begin !!!")
    display_character(character)
    return character





