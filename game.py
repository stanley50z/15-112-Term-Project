class game():
    # MahjongSoul has 3-player mode, 4-player mode, and some special modes
    # In this TP, I would's only do 3-player mode for its simplicity
    # (also I play this mode the most)
    def __init__(self, gameMode = '3p') -> None:
        self.gameMode = gameMode
        self.deck = dict()
        
        self.isRedTileMode = True # on for 4p, off for 3p
        if(self.gameMode == '3p'): self.isRedTileMode = False
        
        self.playerScore = 0
        self.p1Score = 0
        self.p2Score = 0
        self.p3Score = 0
        self.setScore(self)
        
    def setScore(self):
        if(self.gameMode == '3p'):
            #initial points
            self.playerScore = 35000
            self.p1Score = 35000
            self.p2Score = 35000
        else:
            self.playerScore = 25000
            self.p1Score = 25000
            self.p2Score = 25000
            self.p3Score = 25000

            
    def createDeck(self): #pin 筒 sou 条 man 万
        deck = dict()
        if(self.gameMode=='3p'):
            for i in range(1,10): # pin and sou 1 to 9
                deck["s"+str(i)] = 4
                deck["p"+str(i)] = 4
            deck["m1"] = 4        # 3p only has m1&m9, no m2-m8
            deck["m9"] = 4
            for tile in self.WindTiles:     # WindTiles, North is included!
                deck[tile] = 4
            for tile in self.DragonTiles:   # DragonTiles
                deck[tile] = 4
        if(self.isRedTileMode):
                deck["s5"] = 3
                deck["p5"] = 3
                deck["m5"] = 3
                deck["s5R"] = 1
                deck["p5R"] = 1
                deck["m5R"] = 1    
            
    TerminalTiles = ['s1','s9','p1','p9','m1','m9','W','E','N','S','rd','wd','gd'] #幺九牌
    OneNineTiles = ['s1','s9','p1','p9','m1','m9'] #清老头牌
    DragonTiles = ['rd','wd','gd'] #三元牌
    WindTiles = ['W','S','E','N'] #风牌
    WordTiles = DragonTiles + WindTiles #字牌
    AllGreenTiles = ['s2','s3','s4','s6','s8','gd'] #绿一色牌
        