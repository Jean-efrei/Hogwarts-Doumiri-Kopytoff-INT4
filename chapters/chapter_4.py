from universe import character
from utils.input_utils import load_file
import random


def create_team(house, team_data, is_player=False, player=None) :
    house = character["House"]
    team = {}
    team["name"] = house
    team["score"] = 0
    team["has_scored"] = 0
    team["has_stopped"] = 0
    team["caught_snitch"] = False
    teams_quidditch = load_file("data/teams_quidditch.json")
    team["players"] = teams_quidditch["house"]["players"]
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
        print("{} blocks the attack !".format(defending_team["name"))
        blocked_attack = blocked_attack + 1

def golden_snitch_appears():
    snitch = random.randint(1, 6)
    if snitch == 6 :
        return True
    else :
        return False

def catch_golden_snitch(e1, e2) :
    w = random.randint(1, 2)
    if w == 1 :
        e1["Score"] = e1["Score"] + 150
        e1 ["caught_snitch"] = True
    else:
        e2["Score"] = e2["Score"] + 150
        e2["caught_snitch"] = True

def display_score(e1, e2) :
    print("Current Score :")
    print(e1["Name"], ": ", e1["Score"], "points")
    print(e2["Name"], ": ", e2["Score"], "points")

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
    while rounds < 20 :
        rounds = rounds + 1
        print("Round: ", rounds)
        attempt_goal(teams_quidditch[player_house]["players"], opposing_team, player_is_seeker=True)
        attempt_goal(opposing_team, teams_quidditch[opposing_house]["players"])
        display_score(teams_quidditch[player_house]["players"], opposing_team)


















