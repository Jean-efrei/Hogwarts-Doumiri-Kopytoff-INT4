import random
from utils.input_utils import load_file
from universe.house import update_house_points, display_winning_house
from universe.character import display_character


def create_team(house, team_data, is_player=False, player=None) :
        team = {}
        team["name"] = house
        team["score"] = 0
        team["goals_scored"] = 0
        team["goals_blocked"] = 0
        team["caught_snitch"] = False
        players = []
        i = 0
        while i < len(team_data):
            players.append(team_data[i])
            i = i + 1
        if is_player == True and player is not None:
            new_players = []
            seeker = player["First Name"], " " ,player["Last Name"], " (Seeker)"
            new_players.append(seeker)
            i = 0
            while i < len(players):
                if players[i] != seeker:
                    new_players.append(players[i])
                i = i + 1
            players = new_players
        team["players"] = players
        return team


def attempt_goal(attacking_team, defending_team, player_is_seeker=False) :
    chance_goal = random.randint(1, 10)
    if chance_goal >= 6:
        if player_is_seeker:
            scorer = attacking_team["players"][0]
        else:
            idx = random.randint(0, len(attacking_team["players"]) - 1)
            scorer = attacking_team["players"][idx]
            attacking_team["score"] = attacking_team["score"] + 10
            attacking_team["goals_scored"] = attacking_team["goals_scored"] + 1
            print(scorer, " scores a goal for ", attacking_team["name"], "! (+10 points)")
    else:
        defending_team["goals_blocked"] = defending_team["goals_blocked"] + 1
        print(defending_team["name"], " blocks the attack!")


def golden_snitch_appears():
    snitch = random.randint(1, 6)
    if snitch == 6 :
        return True
    else :
        return False

def catch_golden_snitch(e1, e2) :
    w = random.randint(1, 2)
    if w == 1 :
        e1["score"] = e1["score"] + 150
        e1 ["caught_snitch"] = True
        return e1
    else:
        e2["score"] = e2["score"] + 150
        e2["caught_snitch"] = True
        return e2


def display_score(e1, e2) :
    print("Current Score :")
    print(e1["name"], ": ", e1["score"], "points")
    print(e2["name"], ": ", e2["score"], "points")

def display_team(house, team) :
        print(house + " team:")
        i = 0
        while i < len(team["players"]):
            print("- ", team["players"][i])
            i = i + 1


def quidditch_match(character, houses) :
    teams_data = load_file("data/teams_quidditch.json")
    player_house = character["House"]
    house_names = []
    for h in houses:
        house_names.append(h)
    opposing_house = random.choice(house_names)
    while opposing_house == player_house:
        opposing_house = random.choice(house_names)
    player_team = create_team(player_house, teams_data[player_house]["players"], True, character)
    opposing_team = create_team(opposing_house, teams_data[opposing_house]["players"], False, None)

    print("Quidditch Match: ", player_house, " vs ", opposing_house, "!")
    display_team(player_house, player_team)
    display_team(opposing_house, opposing_team)
    print("You are playing for ", player_house, " as the Seeker")
    turn = 1
    match_over = False
    while turn <= 20 and match_over == False:
        print("━━━ Turn " , turn, " ━━━")
        attempt_goal(player_team, opposing_team, True)
        attempt_goal(opposing_team, player_team, False)
        display_score(player_team, opposing_team)
        if golden_snitch_appears() == True:
            winner_team = catch_golden_snitch(player_team, opposing_team)
            print("The Golden Snitch has been caught by ", winner_team["name"], "! (+150 points)")
            match_over = True
        input("Press Enter to continue")
        turn = turn + 1
    print("End of the match!")
    display_score(player_team, opposing_team)
    if player_team["score"] > opposing_team["score"]:
        match_winner = player_team
    elif opposing_team["score"] > player_team["score"]:
        match_winner = opposing_team
    else:
        match_winner = None
    if match_winner is None:
        print("Final result: It's a tie!")
    else:
        print("Final result: Victory for ", match_winner["name"], "!")
        update_house_points(houses, match_winner["name"], 500)
    update_house_points(houses, player_team["name"], player_team["score"])
    update_house_points(houses, opposing_team["name"], opposing_team["score"])

    print(display_winning_house(houses))


def start_chapter_4_quidditch(character, houses):
    print("--- Chapter 4: Quidditch Final ---")
    quidditch_match(character, houses)
    print("End of Chapter 4 — What an incredible performance on the field!")
    print("House Cup status:")

    display_winning_house(houses)
    display_character(character)



















