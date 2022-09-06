from ship import Ship


class Carrier(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Carrier'
        self.size = 5
        self.hits = 0
