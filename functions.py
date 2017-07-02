"""Learning python functions"""
import os
import datetime

os.system('cls')

def log_message(msg):
    """Logs a message"""
    os.system('cls')
    print(f'[{datetime.datetime.today()}] You typed: {msg}')
    return

def get_input():
    """gets the users input"""
    msg = input(f'What would you like to say? ')
    log_message(msg)

    again = input(f'\nAgain? [y / n] ')
    if again == 'Y' or again == 'y':
        get_input()

get_input()
