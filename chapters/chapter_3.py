import json
import random
from universe.character import add_item, display_character
from universe.house import update_house_points, display_winning_house

def learn_spells(character, file_path="data/spells.json"):
    print("You begin your magic lessons at Hogwarts...")

    file = open(file_path, "r", encoding="utf-8")
    spells = json.load(file)
    file.close()

    learned_spells = []
    offensive = 0
    defensive = 0
    utility = 0

    while len(learned_spells) < 5:
        spell = random.choice(spells)

        if spell not in learned_spells:
            if spell["type"] == "Offensive" and offensive < 1:
                learned_spells.append(spell)
                offensive = offensive + 1
            elif spell["type"] == "Defensive" and defensive < 1:
                learned_spells.append(spell)
                defensive = defensive + 1
            elif spell["type"] == "Utility" and utility < 3:
                learned_spells.append(spell)
                utility = utility + 1

    i = 0
    while i < len(learned_spells):
        spell = learned_spells[i]
        character["Spells"].append(spell["name"])

        print("You have just learned the spell: " + spell["name"] + " (" + spell["type"] + ")")
        input("Press Enter to continue...")
        i = i + 1

    print("You have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:")

    i = 0
    while i < len(learned_spells):
        spell = learned_spells[i]
        print("- " + spell["name"] + " (" + spell["type"] + "): " + spell["description"])
        i = i + 1

def magic_quiz(character, file_path="data/magic_quiz.json"):
    print("Welcome to the Hogwarts magic quiz!")
    print("Answer the 4 questions correctly to earn points for your house.")

    file = open(file_path, "r", encoding="utf-8")
    questions = json.load(file)
    file.close()

    selected_questions = []
    score = 0

    while len(selected_questions) < 4:
        question = random.choice(questions)
        if question not in selected_questions:
            selected_questions.append(question)

    i = 0
    while i < len(selected_questions):
        q = selected_questions[i]
        print(str(i + 1) + ". " + q["question"])
        answer = input("> ")

        if answer.lower() == q["answer"].lower():
            print("Correct answer! +25 points for your house.")
            score = score + 25
        else:
            print("Wrong answer. The correct answer was: " + q["answer"])

        i = i + 1

    print("Score obtained: " + str(score) + " points")
    return score

def start_chapter_3(character, houses):
    print("--- Chapter 3: Classes and Discovering Hogwarts ---")

    learn_spells(character)
    quiz_score = magic_quiz(character)
    house_name = character["House"]
    update_house_points(houses, house_name, quiz_score)
    display_winning_house(houses)
    display_character(character)
