class Ship:
    def __init__(self):
        self.name = ''
        self.size = 0
        self.coordinates = None
        self.is_sunk = False
        self.hits = 0

    def set_is_sunk(self):
        self.is_sunk = not self.is_sunk
