from ship import Ship


class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Destroyer'
        self.size = 2
        self.hits = 0
