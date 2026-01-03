""""#TEST CHAPTER 1
from chapters.chapter_1 import start_chapter_1

def main():
    start_chapter_1()

if __name__ == "__main__":
    main()


#TEST CHAPTER 2
from chapters.chapter_2 import start_chapter_2
from universe.character import init_character, display_character

def main():
    attributes = {
        "Courage": 8,
        "Intelligence": 8,
        "Loyalty": 8,
        "Ambition": 8
    }

    character = init_character("Potter", "Harry", attributes)

    print("=== BEFORE CHAPTER 2 ===")
    display_character(character)

    start_chapter_2(character)

    print("\n=== AFTER CHAPTER 2 ===")
    display_character(character)

if __name__ == "__main__":
    main()



#TEST CHAPTER 3
from chapters.chapter_3 import start_chapter_3
from universe.character import init_character, display_character

def main():
    # Création d'un personnage fictif cohérent
    attributes = {
        "Courage": 8,
        "Intelligence": 8,
        "Loyalty": 8,
        "Ambition": 8
    }

    character = init_character("Potter", "Harry", attributes)

    # Le chapitre 3 suppose que la maison est déjà définie
    character["House"] = "Gryffindor"

    # Dictionnaire des maisons avec leurs points
    houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    print("=== BEFORE CHAPTER 3 ===")
    display_character(character)

    print("\n=== START CHAPTER 3 ===\n")
    start_chapter_3(character, houses)

    print("\n=== AFTER CHAPTER 3 ===")
    display_character(character)

    print("\n=== HOUSES SCORES ===")
    for house in houses:
        print(house + ": " + str(houses[house]) + " points")

if __name__ == "__main__":
    main()
"""

#TEST MAIN
from menu import launch_menu_choice

def main():
    launch_menu_choice()

if __name__ == "__main__":
    main()









