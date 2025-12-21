from utils.input_utils import ask_number
from chapters.chapter_1 import start_chapter_1
from chapters.chapter_2 import start_chapter_2
from chapters.chapter_3 import start_chapter_3

def display_main_menu():
    print("\n=== Main Menu ===")
    print("1. Start Chapter 1 – Arrival in the magical world")
    print("2. Exit the game")


def launch_menu_choice():
    houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Ravenclaw": 0,
        "Hufflepuff": 0
    }

    display_main_menu()
    choice = ask_number("Your choice: ", 1, 2)

    if choice == 1:
        introduction()
        character = create_character()

        start_chapter_2(character, houses)
        start_chapter_3(character, houses)
        start_chapter_4(character, houses)

    elif choice == 2:
        print("Thank you for playing. Goodbye!")

    else:
        print("Invalid choice.")
