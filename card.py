class Card:
    def __init__(self, name, type, image1, image2):
        self.name = name
        self.image1 = image1
        self.image2 = image2
        self.type = type

class Entity(Card):
    def __init__(self, name, type, image1, image2, level, atk, defense,):
        super().__init__(name, "Entity", image1, image2)
        self.level = level
        self.atk = atk
        self.defense = defense

class Trap(Card):
    def __init__(self, name, type, image1, image2):
        super().__init__(name, "Trap", image1, image2)

class Magic(Card):
    def __init__(self, name,type, image1, image2):
        super().__init__(name, "Magic", image1, image2)
