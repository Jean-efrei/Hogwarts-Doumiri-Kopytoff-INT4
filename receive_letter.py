from utils.input_utils import ask_choice


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
        print("You tear up your letter, and throw it into the fire place, Uncle Vernon cheers : Finally someone normal in this house !")
        print("The magical world will never hear about, what a wast of magic ! GAME OVER")

