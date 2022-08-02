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
        self.setScore(self)
        
    def setScore(self):
        if(self.gameMode == '3p'):
            #initial points
            self.playerScore = 35000
            self.p1Score = 35000
            self.p2Score = 35000
            
    TerminalTiles = ['s1','s9','p1','p9','m1','m9','W','E','N','S','rd','wd','gd'] #幺九牌
    OneNineTiles = ['s1','s9','p1','p9','m1','m9'] #清老头牌
    DragonTiles = ['rd','wd','gd'] #三元牌
    WindTiles = ['W','S','E','N'] #风牌
    WordTiles = DragonTiles + WindTiles #字牌
    AllGreenTiles = ['s2','s3','s4','s6','s8','gd'] #绿一色牌
        