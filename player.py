from board import Board
from fleet import Fleet


class Player:
    def __init__(self, name):
        self.name = name
        self.fleet = Fleet()
        self.game_board = Board()
        self.target_board = Board()

    def set_name(self):
        user_input = input(f'\nEnter the name for {self.name}: ')
        self.name = user_input

    def display_fleet(self):
        print(f'\nFleet:')
        for ship in self.fleet.ships:
            print(f'  {ship.name} -- Position: {ship.coordinates} | Hits: ({ship.hits}/{ship.size}) | Sunk: {ship.is_sunk}')

    def set_ships(self):
        pass

    def attack_ship(self):
        pass
