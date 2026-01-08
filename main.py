from chapters.chapter_1 import start_chapter_1
from chapters.chapter_2 import start_chapter_2
from chapters.chapter_3 import start_chapter_3
from chapters.chapter_4 import start_chapter_4_quidditch
from menu import display_main_menu
from utils.input_utils import ask_number

def main():

    character = None
    current_chapter = 1

    while current_chapter <= 4:
        display_main_menu(current_chapter)
        choice = ask_number("Your choice: ", 1, 2)

        if choice == 2:
            print("Goodbye!")
            return

        if current_chapter == 1:
            character = start_chapter_1()
        elif current_chapter == 2:
            start_chapter_2(character)
        elif current_chapter == 3:
            start_chapter_3(character, houses)
        elif current_chapter == 4:
            start_chapter_4_quidditch(character, houses)

        current_chapter = current_chapter + 1

    print("")
    print("=== END ===")
    print("Final houses scores:")
    for h in houses:
        print(h, ":", houses[h], "points")


if __name__ == "__main__":
    main()
