from board import Board
from fleet import Fleet


class Player:
    def __init__(self, name):
        self.name = name
        self.fleet = Fleet()
        self.game_board = Board()
        self.target_board = Board()

    def set_name(self):
        pass

    def display_fleet(self):
        pass

    def set_ships(self):
        pass

    def attack_ship(self):
        pass
