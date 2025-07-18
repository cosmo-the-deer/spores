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
buildings = ['crop', 'scare_crow']
building_give_amount = {'crop': 1, 'scare_crow': 10}
building_prices = {'crop': 10, 'scare_crow': 100}
building_amounts = {'crop': 1, 'scare_crow': 1}

def store():
    print('welcome to the store')
    print('type exit to exit')
    while True:
        print()
        command = input('$=').lower()
        print()
        if command == 'buy':
            pass
        elif command == 'sell':
            pass
        elif command == 'exit':
            print('exiting store...')
            time.sleep(1)
            return
        elif command == 'help':
            print_file('store_help.txt')
        elif command == 'clear':
            clear_screen()
        elif command == 'where am i':
            print('store')
        elif command == 'store':
            print('you are allready in the store')
        else:
            print(command + ' is not a valid command')

def calculate_harvest():
    global spores_bonus_harvest, spores_per_multiplyer, spores_per_harvest, building_amounts, buildings, building_give_amount
    spores_per_harvest = 0
    spores_bonus_harvest = 0
    spores_per_multiplyer = 1
    for i in range(len(buildings)):
        spores_per_harvest += building_amounts[buildings[i]] * building_give_amount[buildings[i]]

def start_new_game():
# if you are editing this to make it better please find a way to reload instead of exiting
# this resets the game and saves it to the data.txt file
    global spores, spores_per_harvest, spores_bonus_harvest, spores_per_multiplyer, new_game
    spores = 0
    farm_name = 'dr mylo\'s farm'
    new_game = True
    save()
    exit()

def load():
# this sets the variables to the values in the data.txt file
# it can be called at the start of the game to load the game
# these are global variables so they can be used in the functions
    global spores, spores_per_harvest, spores_bonus_harvest, spores_per_multiplyer, new_game, farm_name
    file = open('data.txt', 'r')
    data = file.readlines()
    file.close()
    spores = int(data[0].replace('spores:', '').strip())
    farm_name = data[1].replace('farm name:', '').strip()
    new_game = data[2].replace('new game:', '').strip() == '1'

def save():
# this function is used to save the game data to the data.txt file
# it is called when the game is exited or when the player wants to save the game
# it uses the global variables to save the data
# it overwrites the data.txt file with the new data
# it is called in the new_game function.
    global spores, spores_per_harvest, spores_bonus_harvest, spores_per_multiplyer, new_game
    file = open('data.txt', 'w')
    file.write('spores: ' + str(spores) + '\n')
    file.write("farm name: " + farm_name + '\n')
    file.write('new game: ' + ('1' if new_game else '0')  + '\n')
    file.close()
    print('game saved successfully')

def print_file(file):
# this function is used to print.txt files and close them
# it is used in the help command and the license command
    with open(file, 'r') as f:
        print(f.read())

def intro():
# this fuction is used to print the intro to the game
# and check if the player has a new game or not
# if the player has a new game it will ask for the name of the farm
# and save it to the data.txt file
# if the player does not have a new game it will print the name of the farm
# it is called at the start of the game
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
#this harvests the spores
    global spores, spores_bonus_harvest, spores_per_harvest, spores_per_multiplyer
    calculate_harvest()
    spores_harvested = spores_per_harvest + spores_bonus_harvest * spores_per_multiplyer
    spores = spores + spores_per_harvest + spores_bonus_harvest * spores_per_multiplyer
    print('harvested spores: ' + str(spores_harvested) + '. total spores: ' + str(spores))

def info():
# this function is used to print the info about the current game
# nts create a func to print the info about the saved game
# this cannot be in a txt file because it is changing
    print('spores: ' + str(spores))
    print('spores per harvest: ' + str(spores_per_harvest))
    print('spores per harvest bonus: ' + str(spores_bonus_harvest))
    print('spores multiplyer: ' + str(spores_per_multiplyer))
    print('farm name: ' + farm_name)

def main():
#gets the players input and stores it in the variable "command"
#then checks i it matches any of the commands
#if it does, it runs the function associated with that command
#if it does not, it prints an error message
#to add a new command, add it to the list of commands useing elif, and create a function for it
    while True:
        command = input('$=').lower()
        print()
    
        if command == 'help':
            print_file('main_help.txt')
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
        elif command == 'store':
            clear_screen()
            store()
            clear_screen()
        elif command == 'where am i':
            print('main menu')
            print()
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