import sys, copy
sys.path.insert(0, '')

from TermProject.tile import tile_constants
from TermProject.player import Player
from TermProject.score import ScoreCounter

# from player import Player
class game():
    # MahjongSoul has 3-player mode, 4-player mode, and some special modes
    # In this TP, I would's only do 3-player mode for its simplicity
    # (also I play this mode the most)
    def __init__(self, coldStart = False, gameMode = '3p') -> None:
        self.gameMode = gameMode
        self.coldStart = coldStart
        
        self.fulldeck = dict()
        self.deck = dict()
        self.remainingTiles = 0
        
        self.isRedTileMode = True # on for Mahjong Soul, other Mahjong games may not have red tiles
        self.players = []
        self.playerScores = []
        self.currentPlayer = 0
        self.lastTile = ''
        self.setScore()
        self.initPlayers()
        self.createDeck()
        self.dealer = 0
        self.dora = ''
        if not self.coldStart:
            self.playGame()
    
    def initPlayers(self):
        player = Player('player')
        p1 = Player('p1')
        p2 = Player('p2')
        self.players.append(player)
        self.players.append(p1)
        self.players.append(p2)
        
        
    def getDealerwind(self):
        # return self.players[self.dealer].getWind()
        return 'E' # will change with a series of games, but for now, East is the most common one
    
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
            for tile in tile_constants.WindTiles:     # WindTiles, North is included!
                deck[tile] = 4
            for tile in tile_constants.DragonTiles:   # DragonTiles
                deck[tile] = 4
            # if(self.isRedTileMode):
            #         deck["s5"] = 3
            #         deck["p5"] = 3
            #         deck["s5R"] = 1
            #         deck["p5R"] = 1
        self.fulldeck = deck
        self.remainingTiles = 4*27
        
    def updateDeck(self):
        deck = copy.deepcopy(self.fulldeck)
        for player in self.players:
            for tile in player.getBoard():
                deck[tile] -= 1
            for group in player.getOpenMelds():
                for tile in group:
                    deck[tile] -= 1
        deck = {k:v for k,v in deck.items() if v!=0}
        self.deck = deck
    
    def countDeck(self):
        count = 0
        for tile in self.deck.keys():
            count += self.deck.get(tile)
        return count
    
    def getChance(self, tile):
        self.updateDeck()
        return self.deck.get(tile,0) / self.countDeck()
    
    def getDora(self,tile):
        if tile in tile_constants.WindTiles:
            winds = ['E','S','W','N','E']
            return winds[winds.index(tile)+1]
        elif tile in tile_constants.DragonTiles:
            dragons = ['wd','gd','rd','wd']
            return dragons[dragons.index(tile)+1]
        else:
            if(self.gameMode =='3p' and tile == 'm1'): return 'm9'
            type,num = tile[0],tile[1]
            if(num != '9'):
                return type + str(int(num)+1)
            else:
                return type+'1'
    def setDora(self,tile):
        self.dora = tile
    @staticmethod
    def listToDict(list:list):
        d = dict()
        for tile in list:
            d[tile] = d.get(tile,0) + 1
        return d
    def deckRemove(self,tile):
        self.fulldeck[tile] -= 1
    
    def setWinds(self):
        playerWind = self.players[0].getWind()
        winds = ['E','S','W','E','S']
        p1Wind,p2Wind = winds[winds.index(playerWind)+1], winds[winds.index(playerWind)+2]
        self.players[1].setWind(p1Wind)
        self.players[2].setWind(p2Wind)
        
    def getDealer(self):
        for i in range(0,3):
            if self.players[i].getWind() == 'E':
                self.dealer = i
         
    def getStart(self):
        dora_indicator = input('Enter Dora Indicator: \n')
        self.setDora(self.getDora(dora_indicator))
        self.deckRemove(dora_indicator)
        # print(f'Dora is now {self.dora}')
        # print(self.deck)
        handList = input('Enter your hand: (split with spaces)\n').split()
        self.players[0].setHand(game.listToDict(handList))
        # playerHand = self.players[0].getHand()
        # print(f"Your hand is {playerHand}")
        wind = input('Enter your wind: \n')
        self.players[0].setWind(wind)
        self.setWinds()
        self.getDealer()
        self.currentPlayer = self.dealer
        
    def printBoard(self):
        for player in self.players:
            playerName = player.getName()
            playerWind = player.getWind()
            playerBoard = player.getBoard()
            playerHand = player.getHand()
            playerOM = player.getOpenMelds()
            print(f'{playerName}: \t'+playerWind, end = '\n\t')
            print('Board:', end = '\n\t')
            print(playerBoard, end = '\n\t')
            print('Hand:', end = '\n\t')
            print(playerHand, end = '\n\t')
            print('OM:', end = '\n\t')
            print(playerOM)
        
    def doAction(self):
        cp = self.currentPlayer
        msg = f"Enter discard/action of player {cp}: \n"
        action = input(msg)
        if(action in tile_constants.AllTiles):
            self.players[cp].discard(action)
            self.lastTile = action
            self.cyclePlayer()
            return False
        elif action == '-a':
            # while(self.doAnalyze()):pass
            return self.doAnalyze()
        elif action == 'pei':
            target = self.currentPlayer
            if(target == 0):
                hand = self.players[target].getHand()
                hand['N'] -= 1
                self.players[0].setHand(hand)
            self.fulldeck['N'] -= 1
            return False
        elif action == 'pon':
            target = int(input("Enter the origin of the action: \n"))
            self.currentPlayer = target
            om = self.players[target].getOpenMelds()
            om.append((self.lastTile,self.lastTile,self.lastTile))
            self.players[target].setOpenMelds(om)
            
            if(target == 0):
                hand = self.players[0].getHand()
                hand[self.lastTile] -= 2
                hand = {k:v for k,v in hand.items() if v!=0}
                self.players[0].setHand(hand)
            
            msg = f"Enter discard of player {target}: \n"
            tile = input(msg)
            self.players[target].discard(tile)
            self.lastTile = tile
            self.cyclePlayer()
            return False
        elif action == 'kan':
            target = int(input("Enter the origin of the action: \n"))
            if(target == 0):
                self.players[0].addAnkan()
                hand = self.players[0].getHand()
                hand[self.lastTile] -= 3
                hand = {k:v for k,v in hand.items() if v!=0}
                self.players[0].setHand(hand)
            om = self.players[target].getOpenMelds()
            om.append((self.lastTile,self.lastTile,self.lastTile,self.lastTile))
            self.players[target].setOpenMelds(om)
            return False
    
    def doAnalyze(self):
        
        
        TenPaiMoves = self.getTenPai(self.players[0])
        avgScore = 0
        yakus = set()
        for discard in TenPaiMoves:
            self.players[0].remove(discard)
            winningTiles = self.getWinningTiles(self.players[0])
            winrate = 0
            
            for tile in winningTiles:
                winrate += self.getChance(tile)
                self.players[0].add(tile)
                scoreCounter = ScoreCounter(self.players[0])
                avgScore += scoreCounter.getScore(self.dora)
                yakus = yakus.union(scoreCounter.getYaku())
                self.players[0].remove(tile)
            self.players[0].add(discard)
            avgScore /= len(winningTiles)
            print([discard,winningTiles,winrate])
        print([yakus,avgScore])
        return True
            
        instruction = '''
        'deck': check remaining deck
        tile: detailed analysis for the tile
        risk: risk analysis for each tile in hand\n
        '''
        action = ''
        # while(action != 'end'):
        #     action = input(instruction)
        #     if(action in self.players[0].getHand().Keys()):
        #         for discard in TenPaiMoves:
        #             self.players[0].remove(discard)
        #             winningTiles = self.getWinningTiles(self.players[0])
        #             avgScore = 0
        #             yakus = []
        #             for tile in winningTiles:
        #                 self.players[0].add(tile)
        #                 scoreCounter = ScoreCounter(self.players[0])
        #                 avgScore += scoreCounter.getScore('self.dora')
        #                 yakus = yakus + scoreCounter.yaku
        #                 self.players[0].remove(tile)
        #             self.players[0].add(discard)
        #             avgScore /= len(winningTiles)
        #             print([discard,yakus,avgScore])
        return False
    def playGame(self, start = False):
        # if not (start or self.coldStart): return
        if self.coldStart and (not start):
                return
        if not self.coldStart:
            self.getStart()
        while True:
            self.printBoard()
            cp = self.currentPlayer
            if(cp==0):
                draw = input("Enter your draw: \n")
                if draw != '':
                    self.players[cp].add(draw)
            while(self.doAction()):
                    pass
    
    def isWin(self, player:Player):
        if player.getHandGroups() != None:
            # print(player.getGroups())
            # score = ScoreCounter(player)
            # print(score.getScore('self.dora'))
            # print(score.yaku)
            # print(score.han)
            # print(score.fu)
            return True
        else:
            return False
    
    def isTenpai(self, player:Player):
        for tile in tile_constants.AllTiles:
            player.add(tile)
            if(self.isWin(player)):
                player.remove(tile)
                return True
            player.remove(tile)
        return False
        pass
    def getTenPai(self, player:Player):
        TenpaiMoves = []
        for tile in player.getHand():
            player.remove(tile)
            if(self.isTenpai(player)):
                TenpaiMoves.append(tile)
            player.add(tile)
        return TenpaiMoves
    def getWinningTiles(self, player:Player):
        winningTiles = set()
        for tile in tile_constants.AllTiles:
            player.add(tile)
            if(self.isWin(player)):
                winningTiles.add(tile)
            player.remove(tile)
        return winningTiles
    
    def test(self,h0,b0,om0,b1,om1,b2,om2,dora_id,wind):
        self.players[0].setHand(h0)
        self.players[0].setBoard(b0)
        self.players[0].setOpenMelds(om0)
        self.players[1].setBoard(b1)
        self.players[1].setOpenMelds(om1)
        self.players[2].setBoard(b2)
        self.players[2].setOpenMelds(om2)
        self.currentPlayer = 0
        self.deckRemove(dora_id)
        self.setDora(self.getDora(dora_id))
        self.players[0].setWind(wind)
        self.setWinds()
        self.getDealer()

        
if __name__ == '__main__':
    
    # game1 = game()
    # N
    # m1 m1     p1 p2 p3     p5 p5 p5    s3 s4     wd wd wd

    # p9
    # p5 p6 p6 p7 p7 s1 s1 s2 s6 s8 S wd gd
    
    # How to test:  uncomment game1 = game()
    #               enter N
    #               enter m1 m1 ...
    #               enter E
    #               enter s6
    #               enter -a
    
    
    game1 = game(coldStart=True)
    h0 = game.listToDict(['p8','p8','s2', 's3', 's4', 's7', 's8'])
    b0 = ['m1','p1','p3','rd','m1','s2']
    om0 = [('m9','m9','m9','m9'),('gd','gd','gd')]
    b1 = ['s1','rd','W','S','wd']
    om1 = []
    b2 = ['m1','S','wd','s2']
    om2 = []
    dora = 's7'
    wind = 'E'
    game1.test(h0,b0,om0,b1,om1,b2,om2,dora,wind)
    game1.playGame(start=True)
    
    # How to test: enter 'W' as the drawn tile
    #              enter '-a' to print a brief analysis
    
    # print(game1.getDora('s5'))
    