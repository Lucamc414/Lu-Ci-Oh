from card import Entity

class AlexDestroyerOfPints(Entity):
    def __init__(self):
        super().__init__("Alex, Destroyer of Pints", "Entity", "images/AlexDestroyerOfPints1.png", "images/AlexDestroyerOfPints2.png",1,1800,700)

    def effect(self):
        self.attack += 200
