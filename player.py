class Player():
    def __init__(self) -> None:
        self.hand = dict() #key: tileType, value: number of tile
        self.openMelds = list() #List of tuples that represent groups
        self.draw = ""
        self.sq = 0 #手切次数
        self.board = dict()
        
    def discard(self, tile) -> bool:
        if(tile not in self.hand.keys()):
            return False
        if(tile == self.draw):
            self.sq += 1
        self.hand[self.draw] += 1
        self.hand[tile] -= 1
        self.board.setdefault(tile,0)
        self.board[tile] += 1
        if self.hand[tile] == 0:
            self.hand.pop(tile)
        return True
            
    def checkWin(self):
        fullHand = dict()
        #add hand
        for tile in self.hand.keys():
            fullHand.setdefault(tile,0)
            fullHand[tile] += self.hand[tile] 
        #add open melds
        for group in self.openMelds:
            for tile in group:
              fullHand.setdefault(tile,0)
              fullHand[tile] += 1   
        #add the drawn
        fullHand.setdefault(self.draw,0)
        fullHand[self.draw] += 1