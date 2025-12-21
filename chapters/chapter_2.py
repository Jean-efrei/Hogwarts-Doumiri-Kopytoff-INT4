from utils.input_utils import ask_choice, load_file
from universe.house import assign_house
import json

def welcome_message():
   print("Welcome to Hogward. I'm Professor Dumbledore. Before we begin our banquet, I would like to say a few words. And here they are: Nitwit! Blubber! Oddment! Tweak! Thank you. You will see, Hogwarts is a place where memories are made, I am sure you will enjoy your time at our school over the next seven years. Welcome again and Bon Appétit !")
   input()





def meet_friends(character):
    print("You board the Hogwarts Express. The train slowly departs northward... A red-haired boy enters your compartment, looking friendly.")
    print("Hi! I'm Ron Weasley. Mind if I sit with you?")
    print("How do you respond?")
    print("1. Sure, have a seat!")
    print("2. Sorry, I prefer to travel alone.")
    x = ask_choice ("Your choice:", ["1", "2"])
    if x == "1":
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
        character["Attributes"]["Loyalty"] += 1
    else:
        print("Okay, I'll get another seat, see you !")
        character["Attributes"]["Ambition"] += 1
    print("A girl enters next, already carrying a stack of books.")
    print("Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    print("How do you respond?")
    print("1. Yes, I love learning new things!")
    print("2. Uh… no, I prefer adventures over books.")
    y = ask_choice("Your choice:", ["1", "2"])
    if y == "1" :
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
        character["Attributes"]["Intelligence"] += 1
    else:
        print("Seriously ? You looked smarter when I saw you by the window. Do you really think you can become an Auror without books ?")
        character["Attributes"]["Courage"] += 1
    print("Then a blonde boy enters, looking arrogant.")
    print("I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?")
    print("How do you respond?")
    print("1. Shake his hand politely.")
    print("2. Ignore him completely.")
    print("3. Respond with arrogance.")
    z = ask_choice("Your choice:", ["1", "2", "3"])
    if z == "1":
        print("I hope we'll be together in Slytherin !")
        character["Attributes"]["Ambition"] += 1
    elif z == "2":
        print("Draco frowns, annoyed. — You'll regret that!")
        character["Attributes"]["Loyalty"] += 1
    else:
        print("HOW DARE YOU ? DO YOU KNOW WHO IS MY FATHER ?")
    print("The train continues its journey. Hogwarts Castle appears on the horizon...")
    print ("Your choices already say a lot about your personality!")
    character["Attributes"]["Courage"] += 1


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
    print("The sorting ceremony begins in the Great Hall... The Sorting Hat observes you for a long time before asking its questions:")
    return assign_house(character, questions)

def enter_common_room(character):
    my_house = sorting_ceremony(character)
    house = load_file("data/houses.json")
    print("You follow the prefects through the castle corridors...")
    print(house[my_house]["emoji"], " ",house[my_house]["description"])
    print(house[my_house]["installation_message"])
    colors = ", ".join(house[my_house]["colors"])
    print("Your house is: ", colors)

def start_chapter_2(character) :
    meet_friends(character)
    welcome_message()
    sorting_ceremony(character)
    enter_common_room(character)
    print("Summary of your information :", character)
    text = """
    Wonderful, you're now an official Hogwarts student ! Have fun discovering the castle and all its secrets, but watch out ! Beware the forbidden forest, word is getting around that dangerous creatures live in there... I wouldn't go that way if I were you... 
    """