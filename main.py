# made by cosmo_the_deer
# i am sorry for the mess of code
# thought i would make a game in python
# dont ask how the new_game function works i have no idea
# spaghetti code

#if you can switch the txt files to json files that would be great

# importing the libraries needed for the game
import random
import time
import os


# initializing the variables needed for the game but they are stored in a file
# they are initialized here so they can be used in the functions to load and save the game
spores = 0
spores_per_harvest = 1
spores_bonus_harvest = 0
spores_per_multiplyer = 1
new_game = True
farm_name = ''


# if you are editing this to make it better please find a way to reload instead of exiting
# this resets the var and saves it to the data.txt file
def start_new_game():
    global spores, spores_per_harvest, spores_bonus_harvest, spores_per_multiplyer, new_game
    spores = 0
    spores_per_harvest = 1
    spores_bonus_harvest = 0
    spores_per_multiplyer = 1
    farm_name = 'dr mylo\'s farm'
    new_game = True
    save()
    exit()


# this sets the variables to the values in the data.txt file
# it can be called at the start of the game to load the game
# these are global variables so they can be used in the functions
def load():
    global spores, spores_per_harvest, spores_bonus_harvest, spores_per_multiplyer, new_game, farm_name
    file = open('data.txt', 'r')
    data = file.readlines()
    file.close()
    spores = int(data[0].replace('spores:', '').strip())
    spores_per_harvest = int(data[1].replace('spores per harvest:', '').strip())
    spores_bonus_harvest = int(data[2].replace('spores bonus harvest:', '').strip())
    spores_per_multiplyer = int(data[3].replace('spores per multiplyer:', '').strip())
    farm_name = data[4].replace('farm name:', '').strip()
    new_game = data[5].replace('new game:', '').strip() == '1'


# this function is used to save the game data to the data.txt file
# it is called when the game is exited or when the player wants to save the game
# it uses the global variables to save the data
# it overwrites the data.txt file with the new data
# it is called in the new_game function.
def save():
    global spores, spores_per_harvest, spores_bonus_harvest, spores_per_multiplyer, new_game
    file = open('data.txt', 'w')
    file.write('spores: ' + str(spores) + '\n')
    file.write('spores per harvest: ' + str(spores_per_harvest) + '\n')
    file.write('spores bonus harvest: ' + str(spores_bonus_harvest) + '\n')
    file.write('spores per multiplyer: ' + str(spores_per_multiplyer) + '\n')
    file.write("farm name: " + farm_name + '\n')
    file.write('new game: ' + ('1' if new_game else '0')  + '\n')
    file.close()
    print('game saved successfully')


# this function is used to print.txt files and close them
# it is used in the help command and the license command
def print_file(file):
    with open(file, 'r') as f:
        print(f.read())


# this fuction is used to print the intro to the game
# and check if the player has a new game or not
# if the player has a new game it will ask for the name of the farm
# and save it to the data.txt file
# if the player does not have a new game it will print the name of the farm
# it is called at the start of the game
def intro():
    global new_game, farm_name
    print('welcome to spores.')
    if new_game == True:
        farm_confirmed = False
        while farm_confirmed == False:
            print('please enter the name of your farm')
            farm_name = input('$=')
            if farm_name == '':
                print('name is blank, exiting...')
                time.sleep(1)
                clear_screen()
                exit()
            print('is this the correct name? (y/n)')
            confirm = input('$=').lower()
            if confirm == 'y':
                farm_confirmed = True
            elif confirm == 'n':
                farm_confirmed = False
            else:
                print('invalid input')
        print('your farm name is called: ' + farm_name)
        new_game = False
        save()
    else:   
        print('welcome back to your farm: ' + farm_name)

def clear_screen():
    if os.name == 'nt':
        os.system('clr')
    elif os.name == 'posix':
        os.system('clear')
    else:
        #replace with a raise error
        print('your system type cannot be cleared')

def harvest():
    #harvests the spores and adds them to the total
    global spores, spores_bonus_harvest, spores_per_harvest, spores_per_multiplyer
    spores_harvested = spores_per_harvest + spores_bonus_harvest * spores_per_multiplyer
    spores = spores + spores_per_harvest + spores_bonus_harvest * spores_per_multiplyer
    print('harvested spores: ' + str(spores_harvested) + '. total spores: ' + str(spores))


# this function is used to print the info about the current game
# nts create a func to print the info about the saved game
# this cannot be in a txt file because it is changing
def info():
    print('spores: ' + str(spores))
    print('spores per harvest: ' + str(spores_per_harvest))
    print('spores per harvest bonus: ' + str(spores_bonus_harvest))
    print('spores multiplyer: ' + str(spores_per_multiplyer))
    print('farm name: ' + farm_name)
    print('new game: ' + str(new_game))


#gets the players input and stores it in the variable "command"
#then checks i it matches any of the commands
#if it does, it runs the function associated with that command
#if it does not, it prints an error message
#to add a new command, add it to the list of commands useing elif, and create a function for it
def main():
    while True:
        command = input('$=').lower()
        print()
    
        if command == 'help':
            print_file('commands.txt')
        elif command == 'intro':
            intro()
        elif command == 'clear':
            clear_screen()
        elif command == 'harvest':
            harvest()
        elif command == 'info':
            info()
        elif command == 'exit':
            print('exiting...')
            time.sleep(1)
            save()
            clear_screen()
            exit()
        elif command == 'load':
            print('loading...')
            load()
            time.sleep(1)
            clear_screen()
            print('loaded successfully')
        elif command == 'save':
            save()
        elif command == 'new game':
            print('are you sure you want to start a new game? (y/n)')
            confirm = input('$=').lower()
            if confirm == 'y':
                start_new_game()
            elif confirm == 'n':
                print('not starting a new game')
            else:
                print('invalid input. exiting...')
                time.sleep(1)
                clear_screen()
        elif command == 'license':
            print_file('LICENSE')

        else:
            print(command + ' is not a valid command')


#the actual game starts here
#this loads the game data from the data.txt file
#it then clears the screen and prints the intro
#it then calls the main function to start the game
load()
clear_screen()
intro()
main()