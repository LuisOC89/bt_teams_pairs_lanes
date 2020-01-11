import os
import csv
import sys

def main():
      
    csv_reader = get_file_reader()
    teams = {}


    input("Press Enter to continue...")

def get_file_reader():
    # GET file location
    dir_path = os.getcwd()
    # print(f"current directory is : {dir_path}")
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
                    return csv_reader
            except Exception as ex:
                input("The file doesn't exist, try again... ")  
        elif user_validation == "n":
            pass
        else:
            input("You entered the wrong character, try again later...")  
            sys.exit()



if __name__ == "__main__":
    main()