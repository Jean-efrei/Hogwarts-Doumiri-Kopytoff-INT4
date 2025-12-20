
def update_house_points(houses, house_name, points):
    if house_name in houses:
        houses[house_name] = houses[house_name] + points

        if points >= 0:
            sign = "+"
        else:
            sign = ""

        print(house_name + "" + sign + str(points) + "points (total: " + str(houses[house_name]))


def display_winning_house(houses):
    if not houses:
        print("No houses to display.")
        return

    max_score = max(houses.values())
    winners = []

    for house in houses:
        if houses[house] == max_score:
            winners.append(house)

    if len(winners) == 1:
        print("The winning house is " + winners[0] + "with " + str(max_score) + " points")
    else:
        print("Tie between the following houses with " +str(max_score) + " points:")
        for house in winners:
            print("- " + house)


def assign_house(character, questions):
    scores = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }

    scores["Gryffindor"] = scores["Gryffindor"] + character.get("courage", 0) * 2
    scores["Slytherin"] = scores["Slytherin"] + character.get("ambition", 0) * 2
    scores["Hufflepuff"] = scores["Hufflepuff"] + character.get("loyalty", 0) * 2
    scores["Ravenclaw"] = scores["Ravenclaw"] + character.get("intelligence", 0) * 2


    for question, choices, houses in questions:
        print(question)
        index = 1
        for choice in choices:
            print(str(index) + ". " + choice)
            index = index + 1

        valid = False
        while not valid:
            try:
                answer = int(input("Your choice: "))
                if answer >= 1 and answer <= len(choices):
                    chosen_house = houses[answer - 1]
                    scores[chosen_house] = scores[chosen_house] + 3
                    valid = True
                else:
                    print("Please choose a valid option.")

    print("\nSummary of scores:")
    for house in scores:
        print(house + ": " + str(scores[house]) + " points")

    final_house = max(scores, key=scores.get)
    return final_house








    
