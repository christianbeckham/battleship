from carrier import Carrier
from battleship import Battleship
from cruiser import Cruiser
from submarine import Submarine
from destroyer import Destroyer


class Fleet:
    def __init__(self):
        self.ships = [Carrier(), Battleship(), Cruiser(),
                      Submarine(), Destroyer()]
