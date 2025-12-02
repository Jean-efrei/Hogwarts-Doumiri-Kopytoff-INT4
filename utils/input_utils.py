def ask_text(message):
    question= input("Enter your character's name: ")
    return question

def ask_number(message, min_val=None, max_val=None):
    num= ask_number("Enter an integer: ")
    if min_val is not None and max_val is not None:
        if num < min_val or num > max_val:
            return("Please enter a number between {} and {}")
        else:
            return message , num

def ask_choice(message, options):
    choice = input("Do you want to continue ? ")
    option_1 = input("1. Yes")
    option_2 = input("2. No")
    if choice == option_1:
        return option_1
    elif choice == option_2:
        return option_2
    else:
        return("Please enter a valid option")

def load_file(file_path):
    with open(file_path) as f:
        return f.read()












