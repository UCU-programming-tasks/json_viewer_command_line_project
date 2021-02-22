"""Module for navigating through JSON files and outputting their parts."""

from typing import Any, Dict, List
import json
from pprint import pprint
from colorama import Fore

COLORS = {
    'green': Fore.GREEN,
    'red': Fore.RED,
    'magenta': Fore.MAGENTA
}


def colorful_print(data: str, color: str = None):
    """
    Print the data with the specified color.
    Available colors: 'green', 'red'. If no color is
    specified or it is not one of the available ones,
    data is printed in black.
    """
    if color not in COLORS:
        print(data)
    else:
        color = COLORS[color]
        print(f"{color}{data}{Fore.RESET}")


def read_json(filename: str) -> Dict:
    """
    Read and transform data from JSON file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)

    return data


def prompt_obj(choices: List[str]) -> str:
    """
    Output a list of choices for the user to choose from.
    Wait until user's input is valid. Return the user's choice.
    """
    print('Available paths:')
    for choice in choices:
        colorful_print(f'  {choice}', 'green')

    while True:
        choice = input(
            'Your choice (to select all, press Enter. To move backwards, put \'<\'): ')

        if choice in ('', '<') or choice in choices:
            return choice

        colorful_print('Error! Please make a valid choice.', 'red')

    return choice


def prompt_list(lst: List[str]) -> str:
    """
    Output a list of choices for the user to choose from.
    Wait until user's input is valid. Return the user's choice.
    """
    print('Range of available list indexes: ', end='')
    colorful_print(f'[0..{len(lst) - 1}]', 'magenta')

    while True:
        choice = input(
            'Your choice (to select all, press Enter To move backwards, put \'<\'): ')

        if choice in ('', '<'):
            return choice

        try:
            choice_idx = int(choice)
        except ValueError:
            colorful_print('Error! Please enter a valid number.', 'red')
            continue

        if 0 <= choice_idx < len(lst):
            return choice_idx

        colorful_print('Error! Index out of range.', 'red')


def print_data(data: Any):
    """
    Print data from the given object. At each step, let the user
    choose whether to move deeper recursively into the given data
    or output a certain pert of it.
    """
    if not isinstance(data, (list, dict)) or not data:
        print(data)
        return None

    if isinstance(data, list):
        choice = prompt_list(data)
    else:
        choice = prompt_obj(data)

    if choice == '':
        pprint(data)
    elif choice == '<':
        return 1
    else:
        exit_code = print_data(data[choice])

        if exit_code == 1:
            return print_data(data)

    return None


def main(filename: str):
    """
    Navigate through a JSON file.
    """
    data = read_json(filename)
    print_data(data)


main('kved.json')
