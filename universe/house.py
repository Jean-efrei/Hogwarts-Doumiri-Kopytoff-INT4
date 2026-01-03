from utils.input_utils import ask_number

def update_house_points(houses, house_name, points):
    if house_name in houses:
        houses[house_name] = houses[house_name] + points

        sign = ""
        if points > 0:
            sign = "+"

        print(house_name + " " + sign + str(points) + " points (total: " + str(houses[house_name]) + ")")
    else:
        print("Warning: house not found.")


def display_winning_house(houses):
    max_score = None

    for house in houses:
        if max_score is None or houses[house] > max_score:
            max_score = houses[house]

    winners = []
    for house in houses:
        if houses[house] == max_score:
            winners.append(house)

    if len(winners) == 1:
        print("The winning house is " + winners[0] + " with " + str(max_score) + " points")
    else:
        print("Tie between the following houses with " + str(max_score) + " points:")
        for house in winners:
            print("- " + house)


def assign_house(character, questions):
    scores = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    attributes = character["Attributes"]

    scores["Gryffindor"] = scores["Gryffindor"] + attributes["Courage"] * 2
    scores["Slytherin"] = scores["Slytherin"] + attributes["Ambition"] * 2
    scores["Hufflepuff"] = scores["Hufflepuff"] + attributes["Loyalty"] * 2
    scores["Ravenclaw"] = scores["Ravenclaw"] + attributes["Intelligence"] * 2

    for question in questions:
        text = question[0]
        choices = question[1]
        houses = question[2]

        print(text)

        i = 1
        for choice in choices:
            print(str(i) + ". " + choice)
            i = i + 1

        answer = ask_number("Your choice: ", 1, len(choices))
        chosen_house = houses[answer - 1]
        scores[chosen_house] = scores[chosen_house] + 3

    print("Summary of scores:")
    for house in scores:
        print(house + ": " + str(scores[house]) + " points")

    final_house = ""
    best_score = None

    for house in scores:
        if best_score is None or scores[house] > best_score:
            best_score = scores[house]
            final_house = house

    return final_house
