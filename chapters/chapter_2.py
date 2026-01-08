from utils.input_utils import ask_number, load_file
from universe.house import assign_house
from universe.character import display_character

def welcome_message():
    print("Professor Dumbledore: Welcome to Hogwarts!")
    print("May your year be filled with wonder, friendship, and discovery.")
    input("Press Enter to continue...")


def meet_friends(character):
    attributes = character["Attributes"]

    print("You board the Hogwarts Express. The train slowly departs northward...")
    print("— Hi! I'm Ron Weasley. Mind if I sit with you?")
    print("1. Sure, have a seat!")
    print("2. Sorry, I prefer to travel alone.")
    choice = ask_number("Your choice: ",1, 2)

    if choice == 1:
        attributes["Loyalty"] = attributes["Loyalty"] + 1
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
    else:
        attributes["Ambition"] = attributes["Ambition"] + 1
        print("Ron nods and leaves.")

    print("")
    print("— Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    print("1. Yes, I love learning new things!")
    print("2. Uh… no, I prefer adventures over books.")
    choice = ask_number("Your choice: ",1, 2)

    if choice == 1:
        attributes["Intelligence"] = attributes["Intelligence"] + 1
        print("Hermione smiles, impressed.")
    else:
        attributes["Courage"] = attributes["Courage"] + 1
        print("Hermione looks doubtful.")

    print("")
    print("— I'm Draco Malfoy. It's best to choose your friends carefully, don't you think?")
    print("1. Shake his hand politely.")
    print("2. Ignore him completely.")
    print("3. Respond with arrogance.")
    choice = ask_number("Your choice: ",1, 3)

    if choice == 1:
        attributes["Ambition"] = attributes["Ambition"] + 1
        print("Draco smirks.")
    elif choice == 2:
        attributes["Loyalty"] = attributes["Loyalty"] + 1
        print("Draco frowns.")
    else:
        attributes["Courage"] = attributes["Courage"] + 1
        print("Draco snaps angrily.")

    print("")
    print("Your updated attributes:", attributes)

def sorting_ceremony(character):
    questions = [
        (
            "You see a friend in danger. What do you do?",
            ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "Which trait describes you best?",
            ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        ),
        (
            "When faced with a difficult challenge, you...",
            ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends", "Analyze the problem"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        )
    ]

    print("The sorting ceremony begins in the Great Hall...")
    print("The Sorting Hat observes you for a long time before asking its questions:")

    house_name = assign_house(character, questions)
    character["House"] = house_name

    print("The Sorting Hat exclaims: ", house_name, "!!!")
    print("You join the ", house_name, " students to loud cheers!")


def enter_common_room(character):
    house_data = load_file("data/houses.json")
    my_house = character["House"]

    print("You follow the prefects through the castle corridors...")

    print(house_data[my_house]["emoji"], " ", house_data[my_house]["description"])
    print(house_data[my_house]["installation_message"])

    colors = ", ".join(house_data[my_house]["colors"])
    print("Your house colors: ", colors)

def start_chapter_2(character):
    meet_friends(character)
    welcome_message()
    sorting_ceremony(character)
    enter_common_room(character)

    print("")
    print("End of Chapter 2 summary:")
    display_character(character)

    print("")
    print("End of Chapter 2! Classes at Hogwarts will begin soon...")

