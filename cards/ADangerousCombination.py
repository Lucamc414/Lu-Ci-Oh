from card import Trap

class ADangerousCombination(Trap):
    def __init__(self):
        super().__init__("A Dangerous Combination","Trap","images/ADangerousCombination1.png", "images/ADangerousCombination2.png")

    def effect(self):
        pass