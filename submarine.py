from ship import Ship


class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Submarine'
        self.size = 3
        self.hits = 0
