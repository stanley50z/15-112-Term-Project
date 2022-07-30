class game():
    # MahjongSoul has 3-player mode, 4-player mode, and some special modes
    # In this TP, I would's only do 3-player mode for its simplicity
    # (also I play this mode the most)
    def __init__(self, gameMode = '3p') -> None:
        self.gameMode = gameMode
        self.deck = dict()
        self.playerScore = 0
        self.p1Score = 0
        self.p2Score = 0
        
    def setScore(self):
        if(self.gameMode == '3p'):
            #initial points
            self.playerScore = 35000
            self.p1Score = 35000
            self.p2Score = 35000
        