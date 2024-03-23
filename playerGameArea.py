class PlayerGameArea:
    def __init__(self, player):
        self.player = player
        self.mainMonsterZone = []
        self.spellTrapZone = []
        self.graveyard = []
        self.fieldZone = None
        self.monsterx = 120
        self.monstery = 280
        self.spellx = 120
        self.spelly = 140