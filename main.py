import time
import random
import os

def clear_screen():
    # Clear the console screen
    os.system('clear')
    print_title()

def print_title():
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

def help():
    clear_screen()
    print('''
'help' - Show this help message
'quit' - Exit the game    
'save' - Save the game
'load_fix' - run this if for some reason the game did not load correctly.
'harvest' - Harvest the crops
'tile' prints the title of the game
''')
    

def main():
    print()
    
    main_input = input('> ').lower()
    if main_input == 'help':
        help()
    elif main_input == 'clear':
        clear_screen()

    else:
        print("Invalid command. Type 'help' for a list of commands.")

clear_screen()
main()