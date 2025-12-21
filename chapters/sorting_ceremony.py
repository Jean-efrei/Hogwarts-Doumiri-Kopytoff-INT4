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

