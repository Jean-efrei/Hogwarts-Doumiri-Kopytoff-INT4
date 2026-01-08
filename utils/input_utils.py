import json

def ask_text(message):
    while True:
        user_input = input(message).strip()
        if user_input != "":
            return user_input
        else:
            print("Please enter a non-empty text.")



def ask_number(message, min_val=None, max_val=None):
    while True:
        text = ask_text(message)
        valid = True
        sign = 1
        start = 0
        value = 0

        if text[0] == '-':
            sign = -1
            start = 1
            if len(text) == 1:
                valid = False

        i = start
        while valid and i < len(text):
            c = text[i]
            if c < '0' or c > '9':
                valid = False
            else:
                value = value * 10 + (ord(c) - ord('0'))
            i += 1

        if valid:
            value *= sign
            if min_val is not None and value < min_val:
                print("Please enter a number between " + str(min_val) + " and " + str(max_val) + ".")
                valid = False
            elif max_val is not None and value > max_val:
                print("Please enter a number between " + str(min_val) + " and " + str(max_val) + ".")
                valid = False

        if valid:
            return value
        else:
            print("Please enter a valid integer")


def ask_choice(message, options):
    print(message)
    for i in range (len(options)):
        print(i+1,".",options[i])
    choice = ask_number("Your choice: ", 1, len(options))
    return options[choice - 1]


def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data














