def welcome_message():
   print("Welcome to Hogward. I'm Professor Dumbledore.")
   input()

def enter_common_room(character):
    print("Entering the common room...")
    input()


from utils.input_utils import ask_choice


def meet_friends(character):
    print("You board the Hogwarts Express. The train slowly departs northward... A red-haired boy enters your compartment, looking friendly.")
    print("Hi! I'm Ron Weasley. Mind if I sit with you?")
    print("How do you respond?")
    print("1. Sure, have a seat!")
    print("2. Sorry, I prefer to travel alone.")
    x = ask_choice ("Your choice:", ["1", "2"])
    if x == "1":
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
    else:
        print("Okay, I'll get another seat, see you !")
    print("A girl enters next, already carrying a stack of books.")
    print("Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    print("How do you respond?")
    print("1. Yes, I love learning new things!")
    print("2. Uh… no, I prefer adventures over books.")
    y = ask_choice("Your choice:", ["1", "2"])
    if y == "1" :
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
    else:
        print("Seriously ? You looked smarter when I saw you by the window. Do you really think you can become an Auror without books ?")
    print("Then a blonde boy enters, looking arrogant.")
    print("I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?")
    print("How do you respond?")
    print("1. Shake his hand politely.")
    print("2. Ignore him completely.")
    print("3. Respond with arrogance.")
    z = ask_choice("Your choice:", ["1", "2", "3"])
    if z == "1":
        print("I hope we'll be together in Slytherin !")
    elif z == "2":
        print("Draco frowns, annoyed. — You'll regret that!")
    else:
        print("HOW DARE YOU ? DO YOU KNOW WHO IS MY FATHER ?")
    print("The train continues its journey. Hogwarts Castle appears on the horizon...")
    print ("Your choices already say a lot about your personality!")


#def welcome_message()


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
    print(questions[0][0])
    print("1 :",questions[0][1][0])
    print("2 :",questions[0][1][1])
    print("3 :",questions[0][1][2])
    print("4 :",questions[0][1][3])
    x = int(input("Your choice :"))
    print(questions[1][0])
    print("1 :",questions[1][1][0])
    print("2 :",questions[1][1][1])
    print("3 :",questions[1][1][2])
    print("4 :",questions[1][1][3])
    y = int(input("Your choice :"))
    print(questions[2][0])
    print("1 :",questions[2][1][0])
    print("2 :",questions[2][1][1])
    print("3 :",questions[2][1][2])
    print("4 :",questions[2][1][3])
    z = int(input("Your choice :"))
    #call the function assign_houses to choose the function
