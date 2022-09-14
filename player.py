from board import Board
from fleet import Fleet


class Player:
    def __init__(self, name):
        self.name = name
        self.fleet = Fleet()
        self.game_board = Board()
        self.target_board = Board()

    def set_name(self):
        user_input = input(f'Enter the name for {self.name}: ')
        self.name = user_input

    def set_ships(self):
        pass

    def attack_ship(self):
        pass
