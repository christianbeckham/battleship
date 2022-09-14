from player import Player
from random import shuffle
import os


class Game:
    def __init__(self):
        self.player_one = Player('Player 1')
        self.player_two = Player('Player 2')
        self.player_sequence = None

    def start_game(self):
        self.clear_console()
        self.display_welcome()
        self.display_rules()
        self.shuffle_players()
        self.run_setup()

    def display_welcome(self):
        print('\n--- BATTLESHIP ---')

    def display_rules(self):
        print('\nOBJECTIVE: Be the first to sink all of your opponent\'s ships.')
        print('Each player will have a fleet of 5 ships.')
        print('\tCarrier    - 5 holes')
        print('\tBattleship - 4 holes')
        print('\tCruiser    - 3 holes')
        print('\tSubmarine  - 3 holes')
        print('\tDestroyer  - 2 holes')
        print('\nRULES:')
        print('\tNumber of Players: 2')
        print('\t*Ships can ONLY be placed in a horizontal or vertical position.')
        print('\t*Ships can NOT overlap other ships.')
        print('\t*Ships can NOT be moved once they are set.')
        self.continue_prompt()
        self.clear_console()

    def shuffle_players(self):
        players = [self.player_one, self.player_two]
        shuffle(players)
        self.player_sequence = players

    def run_setup(self):
        for index, player in enumerate(self.player_sequence):
            self.display_welcome()
            print('\nSETUP:')
            if index == 0:
                print('First opponent:', player.name)
            else:
                print('Second opponent:', player.name)
            self.clear_console()

    def clear_console(self):
        os.system('clear' if os.name == 'posix' else 'cls')

    def continue_prompt(self):
        input('\nPress enter to continue...')
