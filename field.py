import playerGameArea

class Field:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        player1Area = playerGameArea.PlayerGameArea(player1)
        player2Area = playerGameArea.PlayerGameArea(player2)