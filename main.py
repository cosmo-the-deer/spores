import random
import time
import os

spores = 0
spores_per_harvest = 1
spores_bonus_harvest = 0
spores_per_multiplyer = 1
new_game = True
farm_name = ''

#loads the game data from data.txt
def load():
    global spores, spores_per_harvest, spores_bonus_harvest, spores_per_multiplyer, new_game
    file = open('data.txt', 'r')
    data = file.readlines()
    file.close()
    spores = int(data[0].replace('spores:', '').strip())
    spores_per_harvest = int(data[1].replace('spores per harvest:', '').strip())
    spores_bonus_harvest = int(data[2].replace('spores bonus harvest:', '').strip())
    spores_per_multiplyer = int(data[3].replace('spores per multiplyer:', '').strip())
    new_game = data[4].replace('new game:', '').strip().lower() == 'true'

def help():
    print('this is the help menu')

def intro():
    global new_game, farm_name
    print('welcome to spores.')
    if new_game == True:
        farm_confirmed = False
        while farm_confirmed == False:
            print('please enter the name of your farm')
            farm_name = input('$=')
            print('is this the correct name? (y/n)')
            confirm = input('$=').lower()
            if confirm == 'y':
                farm_confirmed = True
            elif confirm == 'n':
                farm_confirmed = False
            else:
                print('invalid input')
        print('Lets start the game!')
        new_game = False
    else:   
        print('welcome back to your farm ' + farm_name)

def clear_screen():
    if os.name == 'nt':
        os.system('clr')
    elif os.name == 'posix':
        os.system('clear')
    else:
        #replace with a raise error
        print('your system type cannot be cleared')

#this will be used for harvesting the sporst
def harvest():
    global spores, spores_bonus_harvest, spores_per_harvest, spores_per_multiplyer
    spores_harvested = spores_per_harvest + spores_bonus_harvest * spores_per_multiplyer
    spores = spores + spores_per_harvest + spores_bonus_harvest * spores_per_multiplyer
    print('harvested spores: ' + str(spores_harvested) + '. total spores: ' + str(spores))

def info():
    print('spores: ' + str(spores))
    print('spores per harvest: ' + str(spores_per_harvest))
    print('spores per harvest bonus: ' + str(spores_bonus_harvest))
    print('spores multiplyer: ' + str(spores_per_multiplyer))
    print('farm name: ' + farm_name)
def main():
    while True:
        #gets the players input and stores it in the command var
        command = input('$=').lower()
        print()

        if command == 'help':
            help()
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
            clear_screen()
            exit()
        elif command == 'load':
            print('loading...')
            load()
            time.sleep(1)
            clear_screen()
            print('loaded successfully')
        else:
            print(command + ' is not a valid command')

load()
clear_screen()
intro()
main()