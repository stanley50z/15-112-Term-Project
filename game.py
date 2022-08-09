import sys
sys.path.insert(0, '')
from TermProject.player import Player

# from player import Player
class game():
    # MahjongSoul has 3-player mode, 4-player mode, and some special modes
    # In this TP, I would's only do 3-player mode for its simplicity
    # (also I play this mode the most)
    def __init__(self, gameMode = '3p') -> None:
        self.gameMode = gameMode
        self.deck = dict()
        
        self.isRedTileMode = True # on for Mahjong Soul, other Mahjong games may not have red tiles
        self.players = []
        self.playerScores = []
        self.currentPlayer = 0
        self.setScore(self)
        self.initPlayers(self)
        self.dealer = 0
    
    def initPlayers(self):
        player = Player()
        p1 = Player()
        p2 = Player()
        self.players.append(player)
        self.players.append(p1)
        self.players.append(p2)
        
    def getDealerwind(self):
        return self.players[self.dealer].getWind()
    
    def setScore(self):
        if(self.gameMode == '3p'):
            #initial points
            self.playerScores = [35000,35000,35000]
        else:
            self.playerScores = [25000,25000,25000]


    
    def cyclePlayer(self,p = None):
        # for chi & pon & kan, the game skip to the player who did the action
        # otherwise, skip to the next player
        if(p != None):
            self.currentPlayer = p
        else:
            if(self.gameMode == '3p'):
                self.currentPlayer = (self.currentPlayer+1)%3
            elif(self.gameMode == '4p'):
                self.currentPlayer = (self.currentPlayer+1)%4
            
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
                    deck["s5R"] = 1
                    deck["p5R"] = 1
            
    
    OneNineTiles = {'s1','s9','p1','p9','m1','m9'} #清老头牌
    DragonTiles = {'rd','wd','gd'} #三元牌
    WindTiles = {'W','S','E','N'} #风牌
    WordTiles = DragonTiles.union(WindTiles) #字牌
    TerminalTiles = OneNineTiles.union(WordTiles) #幺九牌
    AllGreenTiles = {'s2','s3','s4','s6','s8','gd'} #绿一色牌
        