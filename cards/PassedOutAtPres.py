from card import Trap

class PassedOutAtPres(Trap):
    def __init__(self):
        super().__init__("Passed Out At Pres","Trap", "images/PassedOutAtPres1.png", "images/PassedOutAtPres2.png")

    def effect(self):
        pass