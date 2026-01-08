from universe import character
from universe.house import display_winning_house, update_house_points
from utils.input_utils import load_file
import random
from universe.character import display_character


def create_team(house, team_data, is_player=False, player=None) :
    team = {}
    team["name"] = house
    team["score"] = 0
    team["has_scored"] = 0
    team["has_stopped"] = 0
    team["caught_snitch"] = False
    team["players"] = team_data
    if is_player == True :
        new_team = []
        team["players"][0] = "{} {} (seeker)".format(player["First Name"], player["Last Name"])
        for i in team["players"] :
            new_team.append(i)
    team["players"] = new_team
    return team

def attempt_goal(attacking_team, defending_team, player_is_seeker=False) :
    blocked_attack = 0
    goal_counter = 0
    chance_goal = random.randint(1, 10)
    if chance_goal => 6 :
        if player_is_seeker == True :
            print("{} scores a goal for {} (+ 10 points)".format(attacking_team["player"][0], attacking_team["name"])
            goal_counter = goal_counter + 1
        else:
            i = random.randint(1, 6)
            random_player = attacking_team["player"][i]
            print(random_player, "scores a goal for {} (+ 10 points)".format(attacking_team["name"]))
    else:
        print("{} blocks the attack !".format(defending_team["name"]))
        blocked_attack = blocked_attack + 1

def golden_snitch_appears():
    snitch = random.randint(1, 6)
    if snitch == 6 :
        return True
    else :
        return False

def catch_golden_snitch(e1, e2) :
    w = random.choice(1, 2)
    if w == 1 :
        e1["score"] = e1["score"] + 150
        e1 ["caught_snitch"] = True
    else:
        e2["score"] = e2["score"] + 150
        e2["caught_snitch"] = True

def display_score(e1, e2) :
    print("Current Score :")
    print(e1["name"], ": ", e1["score"], "points")
    print(e2["name"], ": ", e2["score"], "points")

def display_team(house, team) :
    print(house, "team :")
    for i in team["players"] :
        print("- {}".format(i))

def quidditch_match(character, houses) :
    teams_quidditch = load_file("data/teams_quidditch.json")
    player_house = character["House"]
    opposing_house = random.choice(houses)
    while opposing_house == player_house :
        opposing_house = random.choice(houses)


    player_team = create_team(player_house, teams_quidditch[player_house]["players"], is_player=True, player = character)
    opposing_team = create_team(opposing_house, teams_quidditch[opposing_house]["players"])

    display_team(player_house, player_team)
    display_team(opposing_house, opposing_team)
    print("Welcome to your first quidditch game ! You will play as a seeker")
    rounds = 0
    while rounds <= 20 :
        rounds = rounds + 1
        print("Round: ", rounds)
        attempt_goal(player_team, opposing_team, player_is_seeker=True)
        attempt_goal(opposing_team, player_team)
        display_score(player_team, opposing_team)

        golden_snitch = golden_snitch_appears()
        if golden_snitch == True :
            print ("The golden snitch just appeared !!! Get ready Seekers !")
            catching_team = catch_golden_snitch(player_team, opposing_team)

            print(catching_team["name"],"just caught the golden snitch. The game is over")
            display_score(player_team, opposing_team)

        input("Press Enter to continue...")
        if rounds == 20 :
            print("The game is over !")
            if player_team["score"] > opposing_team["score"] :
                print(player_team["name"], "win the game !")
                player_team["score"] = player_team["score"] + 500
            if player_team["score"] < opposing_team["score"] :
                print(opposing_team["score"], "win the game !")
                opposing_team["score"] = opposing_team["score"] + 500
            else :
                print("It's a tie ! Nobody wins...")
        update_house_points(houses, player_team["name"], player_team["score"])
        update_house_points(houses, opposing_team["name"], player_team["score"])
        print("Final results")
        display_score(player_team, opposing_team)



def start_chapter_4_quidditch(character, houses) :
    print("Chapter 4 : Quidditch match")
    quidditch_match(character, houses)
    print("This is the end of this incredible quidditch game, the atmosphere is amazing here in Hogwarts, what a performance !")
    print("The winner of the House cup is",)
    display_winning_house(houses)
    print("Here are your informations :")
    display_character(character)




















