from utils.input_utils import *
from universe.character import init_character, display_character
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
    print("Catalog of available items : ")
    for key,value in inventory.items():
        join_catalog = " - ".join(value)
        print(inventory[key], ".", join_catalog, "Galleons, \n")
    print("You have ", character["Money"], "Galleons.")
    print("Remaining required items: " )


