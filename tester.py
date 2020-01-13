import os
import csv
import sys
import random
import copy
import string
import pdb

def main():
    # lanes_and_teams = {
    #     'Pair #1': [{'Team 83': {'Dalton Sorry': 'Lane 6A', "David O'Mygod": 'Lane 5A'}},
    #              {'Team 99': {'Diego Coca': 'Lane 5B', 'Kat MaxCubos': 'Lane 6B'}},
    #              {'Team 86': {'Austin Tailored': 'Lane 6C', 'Austin Texas': 'Lane 5C'}},
    #              {'Team 03': {'Luis Cuban': 'Lane 6D', 'Troy Amazon': 'Lane 5D'}}],
    #     'Pair #2': [{'Team 02': {'Danika Patrykc': 'Lane 8A', 'Whale Willy': 'Lane 7A'}},
    #              {'Team 01': {'Geico Buffet': 'Lane 7B', 'Tiger Wuds': 'Lane 8B'}},
    #              {'Team 82': {'Colin Loser': 'Lane 7C', 'Hal Keys': 'Lane 8C'}}],
    #     'Pair #3': [{'Team 80': {'Ricardo Martinez': 'Lane 10A', 'Teddy Crux': 'Lane 9A'}},
    #              {'Team 81': {'Jamie Bailes': 'Lane 9B', 'Jorge Snyder': 'Lane 10B'}},
    #              {'Team 84': {'Marco Aurelious': 'Lane 10C', 'Tim Merlin': 'Lane 9C'}},
    #              {'Team 85': {'Chip DeMexico': 'Lane 9D', 'Khaleel Krypton': 'Lane 10D'}}],
    #     'Pair #4': [{'Team 87': {'Darion Byte': 'Lane 12A', 'Tirus Rex': 'Lane 11A'}},
    #              {'Team 88': {'Billy ElNino': 'Lane 11B', 'Steve Brown': 'Lane 12B'}},
    #              {'Team 100': {'Rafa Peque�o': 'Lane 12C', 'Stephanie McFerrari': 'Lane 11C'}}]}
    
    # Want: Team | Name | Lane 


    with open('lanes_and_teams.csv', mode='w') as lanes_and_teams_doc:
        csv_writer = csv.writer(lanes_and_teams_doc, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['Team', 'Name', 'Lane'])
        pdb.set_trace()
        for k, pair in lanes_and_teams.items():
            for team_dicts in pair:
                team = list(team_dicts.keys())[0]
                for players_dict in team_dicts.values():
                    for name, lane in players_dict.items():
                        csv_writer.writerow([team, name, lane])

if __name__ == "__main__":
    main()