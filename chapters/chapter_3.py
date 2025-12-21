import json
import random
from universe.character import display_character

def learn_spells(character, file_path="../data/spells.json"):
    print("\nYou begin your magic lessons at Hogwarts...")

    file = open(file_path, "r")
    spells = json.load(file)
    file.close()

    learned_spells = []

    offensive = 0
    defensive = 0
    utility = 0

    while len(learned_spells) < 5:
        spell = random.choice(spells)

        if spell in learned_spells:
            pass
        else:
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
        character["spells"].append(spell)

        print("You have just learned the spell: " + spell["name"] + " (" + spell["type"] + ")")
        input("Press Enter to continue...")
        i = i + 1

    print("\nYou have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:")

    i = 0
    while i < len(character["spells"]):
        spell = character["spells"][i]
        print("- " + spell["name"] + " (" + spell["type"] + "): " + spell["description"])
        i = i + 1

def magic_quiz(character, file_path="../data/magic_quiz.json"):
    print("\nWelcome to the Hogwarts magic quiz!")
    print("Answer the 4 questions correctly to earn points for your house.")

    file = open(file_path, "r")
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
    character["score"] = score

def start_chapter_3(character, houses):
    print("\n--- Chapter 3: Classes and Discovering Hogwarts ---")

    learn_spells(character)
    magic_quiz(character)
    house = character["house"]
    houses[house] = houses[house] + character["score"]
    best_house = None
    best_score = -1

    for h in houses:
        if houses[h] > best_score:
            best_house = h
            best_score = houses[h]

    print("\nCurrent leading house: " + best_house + " with " + str(best_score) + " points")
    display_character(character)
