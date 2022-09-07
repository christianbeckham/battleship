from player import Player


class Game:
    def __init__(self):
        self.player_one = Player('Player 1')
        self.player_two = Player('Player 2')

    def start_game(self):
        self.display_welcome()
        self.player_setup(self.player_one)
        self.player_setup(self.player_two)

    def display_welcome(self):
        print('\nWelcome to Battleship!')

    def player_setup(self, player):
        player.set_name()
        player.display_fleet()
