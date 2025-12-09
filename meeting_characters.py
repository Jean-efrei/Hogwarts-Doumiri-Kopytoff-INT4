def meet_friends(character):
    print("You board the Hogwarts Express. The train slowly departs northward... A red-haired boy enters your compartment, looking friendly.")
    print("Hi! I'm Ron Weasley. Mind if I sit with you?")
    print("How do you respond?")
    print("1. Sure, have a seat!")
    print("2. Sorry, I prefer to travel alone.")
    x = int(input("Your choice:"))
    if x == 1:
        print("Ron smiles: — Awesome! You'll see, Hogwarts is amazing!")
        if x == 2:
            print("Okay, I'll get another seat, see you !")
    print("A girl enters next, already carrying a stack of books.")
    print("Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?")
    print("How do you respond?")
    print("1. Yes, I love learning new things!")
    print("2. Uh… no, I prefer adventures over books.")
    y = int(input("Your choice:"))
    if y == 1 :
        print("Hermione smiles, impressed: — Oh, that's rare! You must be very clever!")
        if y == 2:
            print("Seriously ? You looked smarter when I saw you by the window. Do you really think you can become an Auror without books ?")
    print("Then a blonde boy enters, looking arrogant.")
    print("I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?")
    print("How do you respond?")
    print("1. Shake his hand politely.")
    print("2. Ignore him completely.")
    print("3. Respond with arrogance.")
    z = int(input("Your choice:"))
    if z == 1:
        print("I hope we'll be together in Slytherin !")
        if z == 2:
            print("Draco frowns, annoyed. — You'll regret that!")
            if z == 3:
                print("HOW DARE YOU ? DO YOU KNOW WHO IS MY FATHER ?")
    print("The train continues its journey. Hogwarts Castle appears on the horizon...")
    print ("Your choices already say a lot about your personality!")