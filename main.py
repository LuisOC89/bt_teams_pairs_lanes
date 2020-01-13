import os
import csv
import sys
import random
import pdb

def main():
      
    file_path, file_name = get_file_data()
    
    teams = create_teams_dict(file_path)

    show_teams_dict(teams, file_name)
    
    see_specific_team(teams)

    total_pairs, max_teams_per_pair, initial_lane = insert_pairs_and_lanes(teams)
    
    pairs_and_teams = handle_pairs_and_teams(teams, total_pairs, max_teams_per_pair, initial_lane)
    
    # teams_and_lanes = 

    input("\nPress Enter to continue...")

def get_file_data():
    # GET file directory location
    dir_path = os.getcwd()
    
    # Try to get file name until valid
    while True:
        file_name = input("\nPlease insert the *.csv file name and press ENTER... ")
        file_name = f"{file_name}.csv"
        file_path = os.path.join(dir_path, file_name)
        print("current field path is: " + file_path)  
        user_validation = input("Is this correct ([y]/n)?")
        if not user_validation or user_validation == "y":
            try:
                with open(file_path) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    return file_path, file_name
            except:
                input("The file doesn't exist, try again... ")  
        else:
            pass

def create_teams_dict(file_path):
    # teams = {"1":["Luis", "Danika"]}
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        teams = {}
        row_count = 0
        for row in csv_reader:
            if row_count != 0:
                if row[0] != "0":
                    pre = ""
                    if len(row[1]) < 2:
                        pre = "0"    
                    if f"Team {row[1]}" in list(teams.keys()):
                        teams[f"Team {pre}{row[1]}"].append(row[0])
                    else:
                        teams[f"Team {pre}{row[1]}"] = [row[0]]
            row_count += 1
        # print(f"Teams dict: {teams}")
    return teams

def show_teams_dict(teams_dict, file_name):
    print(f"\nTOTAL TEAMS: {len(teams_dict.keys())}")
    while True:
        user_validation = input(f"Would you like to see all the teams recorded from {file_name} ([y]/n)?")
        if not user_validation or user_validation == "y":
            for k, v in teams_dict.items():
                print(f"\n{k}:")
                for player in v:
                    print(player)
            print(f"\nTOTAL TEAMS: {len(teams_dict.keys())}")
            break
        elif user_validation == "n":
            break
        else:
            pass
    
def insert_pairs_and_lanes(teams):
    teams_quantity = len(teams.keys())
    while True:
        pairs = input("\nHow many pairs of lanes there will be? ")
        try:
            pairs_int = int(pairs)
            pairs_float = float(pairs)
            if pairs_int != pairs_float or pairs_int <= 0:
                raise Exception
            total_pairs = pairs_int
        except:
            input("The value of pairs has to be a whole positive number, please try again... ")
            continue

        while True:
            max_teams_per_pair = input("\nWhat will be the max amount of teams per pair of lanes? ")
            try:
                teams_per_pair_int = int(max_teams_per_pair)
                teams_per_pair_float = float(max_teams_per_pair)
                if teams_per_pair_int != teams_per_pair_float or teams_per_pair_int <= 0:
                    raise Exception
                teams_per_pair = teams_per_pair_int
                break
            except:
                input("The value of teams per pair has to be a whole positive number, please try again... ")
                continue
        
        capacity = teams_per_pair * total_pairs
        if capacity < teams_quantity:
            print(f"capacity = {total_pairs} pairs of lanes * {teams_per_pair} teams per pair = {capacity} spaces available.")
            input(f"Number of teams ({teams_quantity} teams) exceeds the capacity " 
            f"({capacity} spaces available) of the place.\nPlease try again... ")
        else:
            break

    while True:
        starting_lane_number = input("\nWhat will be the starting odd lane number? ")
        try:
            lane_int = int(starting_lane_number)
            lane_float = float(starting_lane_number)
            if lane_int != lane_float or lane_int <= 0 or lane_int % 2 == 0:
                raise Exception
            initial_lane = lane_int
            break
        except:
            input("The value of the first lane has to be a whole odd positive number, please try again... ")
    
    print(f"\nTotal teams: {teams_quantity}\nTotal pairs of lanes: {total_pairs}"
        f"\nMax teams per lane: {teams_per_pair}\nInitial odd lane number: {initial_lane}")

    return total_pairs, max_teams_per_pair, initial_lane

def see_specific_team(teams):
    while True:
        user_validation = input(f"\nWould you like to see a specific team's players? ([y]/n)?")
        if not user_validation or user_validation == "y":
            team_number = input(f"What team? (team #)?")
            if f"Team {team_number}" in teams.keys():
                print(f"\nTeam {team_number}")
                for player in teams[f"Team {team_number}"]:
                    print(player)
                continue
            else:
                print("That team # doesn't exist.")
        elif user_validation == "n":
            break
        else:
            pass

def handle_pairs_and_teams(teams, total_pairs, max_teams_per_pair, initial_lane):
    # filled_pairs_of_lanes_list = ["Pair1", "Pair2", "Pair3"]
    # filled_pairs_team_players_dict = {
    #     "Pair1":[
    #         {"Team1":["Player1", "Player2"]},
    #         {"Team2":["Player1", "Player2"]}
    #     ]}
    
    # filled_pairs_team_players_lanes_dict = {
    #     "Pair1":[
    #         {"Team1":{"Player1": "Lane 3A", "Player2": "Lane 4A"}},
    #         {"Team2":{"Player1": "Lane 3B", "Player2": "Lane 4B"}}
    #     ]}

    
    filled_pairs_of_lanes = []
    available_pairs_of_lanes = []
    ordered_available_pairs_of_lanes = []
    available_teams_list = list(teams.keys())

    filled_pairs_team_players_dict = {}
    available_pairs_team_players_dict = {}

    for i in range(1, total_pairs + 1):
        available_pairs_of_lanes.append(f"Pair #{i}")
        available_pairs_team_players_dict[f"Pair #{i}"] = []
    
    while True:
        user_validation = input(f"\nWould you like to prefill a pair of lanes partially or totally with custom teams? ([y]/n)?")
        if user_validation == "y":
            print(f"\navailable_pairs_of_lanes: {available_pairs_of_lanes}"
            f"\nfilled_pairs_of_lanes_list: {filled_pairs_of_lanes}"
            f"\navailable_pairs_team_players_dict: {available_pairs_team_players_dict}"
            f"\nfilled_pairs_team_players_dict: {filled_pairs_team_players_dict}"
            f"\navailable_teams_list: {available_teams_list}")
            
            pair_number = input(f"\nWhat pair #?")
            if f"Pair #{pair_number}" in available_pairs_of_lanes:
                pair_spaces_taken = len(available_pairs_team_players_dict[f"Pair #{pair_number}"])
                team_numbers = input(f"Please insert what team #s you would like to add to this pair (comma separated, no spaces): ")
                try:
                    team_numbers = team_numbers.split(",")
                    for number in team_numbers:
                        if f"Team {number}" not in teams.keys():
                            raise Exception(f"Team {number} doesn't exist, please try again... ")  
                    if len(team_numbers) + pair_spaces_taken > max_teams_per_pair:
                        print(f"Pair #{pair_number}\n")
                        for team in available_pairs_team_players_dict[f"Pair #{pair_number}"]:
                            print(team)
                        print(f"Spaces already taken in Pair #{pair_number}: {pair_spaces_taken}"
                              f"\nNew teams to add to this Pair: {team_numbers}"
                              f"\nMax amount allowed for teams per pair : {max_teams_per_pair}"
                              f"\nThe amount of teams you entered ({team_numbers}) plus spaces taken already in " 
                              f"that pair exceed the max amount allowed for teams per pair ({max_teams_per_pair}), please try again... ")
                        raise Exception("Max amount allowed for teams per pair exceeded, please try again... ")
                    else:
                        # TODO: WHat to do when there are still spaces available
                        # filled_pairs_team_players_dict = {
                        #     "Pair1":[
                        #         {"Team1":["Player1", "Player2"]},
                        #         {"Team2":["Player1", "Player2"]}
                        #     ]}
                        print(f"\nSelected Pair: #{pair_number}")
                        if f"Pair #{pair_number}" in filled_pairs_team_players_dict.keys():
                            for team in filled_pairs_team_players_dict[f"Pair #{pair_number}"]:
                                print(team.keys()[0])
                                for player in [team.values()]:
                                    print(player)
                        elif f"Pair #{pair_number}" not in filled_pairs_team_players_dict.keys():
                            print("Empty pair")
                        print(f"Teams to add:")
                        for number in team_numbers:
                            print(f"Team {number}")
                            for player in teams[f"Team {number}"]:
                                print(player)
                        user_validation = input(f"\nIs this correct (y/n)?")
                        if user_validation != "y":
                            continue
                        for number in team_numbers:
                            team_dict = {} 
                            team_dict[f"Team {number}"] = teams[f"Team {number}"]
                            if f"Pair #{pair_number}" in filled_pairs_team_players_dict.keys():
                                filled_pairs_team_players_dict[f"Pair #{pair_number}"].append(team_dict)
                            else:
                                filled_pairs_team_players_dict[f"Pair #{pair_number}"] = [team_dict]
                            available_teams_list.remove(f"Team {number}")

                        if len(filled_pairs_team_players_dict[f"Pair #{pair_number}"]) == max_teams_per_pair:
                            # filled_pairs_of_lanes.append(f"Pair #{pair_number}")
                            # available_pairs_of_lanes.remove(f"Pair #{pair_number}")
                            filled_pairs_of_lanes.append(available_pairs_of_lanes.pop(available_pairs_of_lanes.index(f"Pair #{pair_number}")))
                except Exception as ex:
                    print(ex)   
                    continue  
            else:
                print("That pair # doesn't exist or is not available.")
        elif user_validation == "n":
            # Random order
            # Start filling dicts by the ones that have less values
            # Example:
            # filled_pairs_team_players_dict = {
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
            #     ],
            #     "Pair4":[]
            # }
            # Start filling Pair4 first
            
            index = 0
            for index in range(max_teams_per_pair):
                for pair_number in available_pairs_of_lanes:
                    # If there is already data there
                    if len(available_pairs_team_players_dict[pair_number]) > index:
                        # DO NOTHING
                        pass
                    elif len(available_pairs_team_players_dict[pair_number]) <= index:
                        random_team = random.choice(available_teams_list)

                        print(f"\nPair: #{pair_number}")
                        if f"Pair #{pair_number}" in filled_pairs_team_players_dict.keys():
                            for team in filled_pairs_team_players_dict[f"Pair #{pair_number}"]:
                                print(team.keys()[0])
                                for player in [team.values()]:
                                    print(player)
                        elif f"Pair #{pair_number}" not in filled_pairs_team_players_dict.keys():
                            print("Empty pair")
                        print(f"Team to add:")
                        print(f"Team {random_team}")
                        for player in teams[f"Team {random_team}"]:
                            print(player)
                        
                        team_dict = {} 
                        team_dict[f"Team {random_team}"] = teams[f"Team {random_team}"]
                        if f"Pair #{pair_number}" in filled_pairs_team_players_dict.keys():
                            filled_pairs_team_players_dict[f"Pair #{pair_number}"].append(team_dict)
                        else:
                            filled_pairs_team_players_dict[f"Pair #{pair_number}"] = [team_dict]
                        available_teams_list.remove(f"Team {random_team}")

                        if len(filled_pairs_team_players_dict[f"Pair #{pair_number}"]) == max_teams_per_pair:
                            # filled_pairs_of_lanes.append(f"Pair #{pair_number}")
                            # available_pairs_of_lanes.remove(f"Pair #{pair_number}")
                            filled_pairs_of_lanes.append(available_pairs_of_lanes.pop(available_pairs_of_lanes.index(f"Pair #{pair_number}")))
                
                if len(available_teams_list) == 0:
                    print(f"\navailable_pairs_of_lanes: {available_pairs_of_lanes}"
                    f"\nfilled_pairs_of_lanes_list: {filled_pairs_of_lanes}"
                    f"\navailable_pairs_team_players_dict: {available_pairs_team_players_dict}"
                    f"\nfilled_pairs_team_players_dict: {filled_pairs_team_players_dict}"
                    f"\navailable_teams_list: {available_teams_list}")
                    break
        else:
            pass

    return filled_pairs_team_players_dict

if __name__ == "__main__":
    main()