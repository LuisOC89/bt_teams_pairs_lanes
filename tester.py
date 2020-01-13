import os
import csv
import sys
import random
import copy
import string
import pdb

def main():
    # pairs_team_players_dict = {
    #     "Pair1":[
    #         {"Team1":["Player1", "Player2"]},
    #         {"Team2":["Player1", "Player2"]}
    #     ],
    #     "Pair2":[
    #         {"Team1":["Player1", "Player2"]},
    #         {"Team2":["Player1", "Player2"]},
    #         {"Team3":["Player1", "Player2"]}
    #     ],
    #     "Pair3":[
    #         {"Team1":["Player1", "Player2"]}
    #     ]
    # }

    new_children = []
    counter_odd = 3
    children = [
        {"Team1":["Player1", "Player2"]},
        {"Team2":["Player1", "Player2"]}
    ]
    pdb.set_trace()
    # Desired
    # new_children = [
    #     {"Team1":{"Player1": "Lane 1A", "Player2": "Lane 2A"}},
    #     {"Team2":{"Player1": "Lane 1B", "Player2": "Lane 2B"}}
    # ]

    # From: {"Team1":["Player1", "Player2"]}
    # To: {"Team1":{"Player1": "Lane 3A", "Player2": "Lane 4A"}}

    # new_children.append(dict.fromkeys(child.keys(),{}))

    possible_lane_letters = list(string.ascii_uppercase)
    
    letter_counter = 0
    for child in children:
        letter = possible_lane_letters[letter_counter]
        tmp_dict = {}
        tmp_dict[list(child.keys())[0]] = {}
        for value in list(child.values())[0]:
            if ((list(child.values())[0]).index(value) + 1) % 2 == 0:
                tmp_dict[list(child.keys())[0]][value] = f"Lane {counter_odd + 1}{letter}"
            else:
                tmp_dict[list(child.keys())[0]][value] = f"Lane {counter_odd}{letter}"
            
        new_children.append(tmp_dict)
        letter_counter += 1

    counter_odd += 2

    return new_children

if __name__ == "__main__":
    main()