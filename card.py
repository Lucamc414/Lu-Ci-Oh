class Card:
    def __init__(self, name, level, attack, defense, type, image1, image2):
        self.name = name
        self.level = level
        self.attack = attack
        self.defense = defense
        self.type = type
        self.image1 = image1
        self.image2 = image2
    
    def effect(self):
        pass
