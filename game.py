from player import Player


class Game:
    def __init__(self):
        self.player_one = Player('Player 1')
        self.player_two = Player('Player 2')

    def start_game(self):
        self.display_welcome()

    def display_welcome(self):
        print('\nWelcome to Battleship!')
