class Player:
    def __init__(self, name):
        self.name = name
        self.lp = 8000
        self.hand = []
        self.deck = []
        self.graveyard = []
        self.field = []