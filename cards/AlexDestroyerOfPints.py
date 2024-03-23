from card import Card

class AlexDestroyerOfPints(Card):
    def __init__(self):
        super().__init__("Alex, Destroyer Of Pints", 1, 1800, 700, "Entity", "images/AlexDestroyerOfPints1.png", "images/AlexDestroyerOfPints2.png")

    def effect(self):
        self.attack += 200
