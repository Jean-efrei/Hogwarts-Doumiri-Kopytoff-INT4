from utils.input_utils import ask_text, ask_number
from universe.character import init_character, display_character


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
        exit(0)
    print("\nYou clutch the letter tightly. Your life will never be the same again...")












