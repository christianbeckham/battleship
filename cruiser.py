from ship import Ship


class Cruiser(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Cruiser'
        self.size = 3
        self.hits = 0
