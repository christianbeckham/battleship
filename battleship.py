from ship import Ship


class Battleship(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Battleship'
        self.size = 4
        self.hits = 0
