from battleship import Battleship
from carrier import Carrier
from cruiser import Cruiser
from destroyer import Destroyer
from submarine import Submarine


class Fleet:
    def __init__(self):
        self.ships = [Carrier(), Battleship(), Cruiser(),
                      Submarine(), Destroyer()]

    def display(self):
        print(f'\nFleet:')
        for ship in self.ships:
            print(
                f'  {ship.name} -- Position: {ship.coordinates} | Hits: ({ship.hits}/{ship.size}) | Sunk: {ship.is_sunk}')
