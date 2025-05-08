import random
import time
import os


def gyn():
    # Ask the user for confirmation
    # and return True for 'y' and False for 'n'

    y_n = ''

    while y_n != 'y' and y_n != 'n':
        reset_screen()
        print('Are you sure? y/n')
        y_n = input().lower()
    return y_n == 'y'

def print_title():
    # Print the title of the game
    print('''
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || |   ______     | || |     ____     | || |  _______     | || |  _________   | || |    _______   | |
| |   /  ___  |  | || |  |_   __ \   | || |   .'    `.   | || | |_   __ \    | || | |_   ___  |  | || |   /  ___  |  | |
| |  |  (__ \_|  | || |    | |__) |  | || |  /  .--.  \  | || |   | |__) |   | || |   | |_  \_|  | || |  |  (__ \_|  | |
| |   '.___`-.   | || |    |  ___/   | || |  | |    | |  | || |   |  __ /    | || |   |  _|  _   | || |   '.___`-.   | |
| |  |`\____) |  | || |   _| |_      | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |___/ |  | || |  |`\____) |  | |
| |  |_______.'  | || |  |_____|     | || |   `.____.'   | || | |____| |___| | || | |_________|  | || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
''')

def reset_screen():
    # Clear the console screen
    # This works for both Windows and Unix-like systems
    os.system('cls' if os.name == 'nt' else 'clear')
    print_title()

def print_help():
    reset_screen()
    print('''
'help' - Show this help message
'harvest' - harvest all plots
'buy' - buy a plot
'sell' - sell a plot
'upgrades' - show available upgrades
'load' if for some reason you need to load a save file
'quit' - quit the game
'clear' - clear the screen
'stats' - show your stats
''')
    
def main():
    reset_screen()
    main_input = ''

    while True:

        main_input = input('> ').lower()

        if main_input == 'help':
            print_help()
        elif main_input == 'quit':
            if gyn():
                os.system('cls' if os.name == 'nt' else 'clear')
                exit()
            else:
                reset_screen()
        elif main_input == 'clear':
            reset_screen()
        elif main_input == 'hug':
            print('you hug mylo')
            time.sleep(1)
            print('mylo hugs you back')
            time.sleep(2)
            reset_screen()
        else:
            print('invalid command type "help" to see a list of commands')
            time.sleep(1)
            reset_screen()
        



        # Add more commands here
        # For example:
        # elif main_input == 'harvest':
        #     harvest_all_plots()
        # elif main_input == 'buy':
        #     buy_plot()
        # elif main_input == 'sell':
        #     sell_plot()
        # elif main_input == 'upgrades':
        #     show_upgrades()

main()