import copy
import string
from turtle import pos

class Player():
    def __init__(self):
        self.hand = dict() #key: tileType, value: number of tile
        self.openMelds = list() #List of tuples that represent groups
        self.board = list()
        
        self.draw = "s5"
        self.wind = "E"
        self.sq = 0 #手切次数

        
    def discard(self, tile):
        if(tile not in self.hand.keys()):
            return False
        if(tile == self.draw):
            self.sq += 1
        self.hand[self.draw] += 1
        self.hand[tile] -= 1
        #I have thought about doing an addTile/removeTile function, 
        # but self.board = self.addTile(tile,self.board) is not that shorter
        self.board[tile] = self.board.get(tile,0)+1 
        if self.hand[tile] == 0:
            self.hand.pop(tile)
        return True
    
    def isLegal(self,dict):
        for v in dict.values():
            if v < 0:
                return False
        return True

    def getGroup(self,tile): 
        possibleGroups = [(tile,tile)] #every 3 of a kind is a group
        type = tile[0]
        if(type=='p' or type=='s' or type=='m'):
            # yes, this looks kinda dumb, but I can't think of a smart way to do it
            # plus there are only 4 situations, which is not that bad
            num = int(tile[1])
            if num == 1 or num == 2:
                possibleGroups.append((type+str(3-num), type+'3'))
                if num == 2: possibleGroups.append((type+str(num+1),type+str(num+2)))
            elif num == 8 or num == 9:
                # if 8, (7,9), if 9, (7,8)
                possibleGroups.append((type+'7',type+str(17-num)))
                # if 8, (6,7)
                if num == 8: possibleGroups.append((type+str(num-2),type+str(num-1)))
            else:
                possibleGroups.append((type+str(num-2),type+str(num-1)))
                possibleGroups.append((type+str(num-1),type+str(num+1)))
                possibleGroups.append((type+str(num+1),type+str(num+2)))
        return possibleGroups
        
    def dfsSearchGroup(self,dict):
        if(not self.isLegal(dict)): return False
        if(sum(dict.values())==2): #when only 2 tiles left, it should be a two of a kind
            return len(dict.keys())==1
        else:
            tile = ""
            for t in dict.keys():
                tile = t
                old = copy.deepcopy(dict)
                for group in self.getGroup(tile):
                    dict[tile] = dict.get(tile,0)-1
                    dict[group[0]] = dict.get(group[0],0)-1
                    dict[group[1]] = dict.get(group[1],0)-1
                    dict = {k:v for k,v in dict.items() if v!=0} # clear zeros so the next first tile is valid
                    if(self.dfsSearchGroup(dict)):
                        return True
                    dict = copy.deepcopy(old)
            return False
               
    def checkWin(self, draw = None):
        if draw == None:
            draw = self.draw
        hand = copy.deepcopy(self.hand)
        #add the drawn tile
        hand[self.draw] = hand.get(self.draw,0)+1
        if not self.dfsSearchGroup(hand): return False #Finished checking basic pattern, now check yaku
        
        return True
    
    def addSQ(self):
        self.sq += 1

    #  ██████╗ ███████╗████████╗       ██╗       ███████╗███████╗████████╗
    # ██╔════╝ ██╔════╝╚══██╔══╝       ██║       ██╔════╝██╔════╝╚══██╔══╝
    # ██║  ███╗█████╗     ██║       ████████╗    ███████╗█████╗     ██║   
    # ██║   ██║██╔══╝     ██║       ██╔═██╔═╝    ╚════██║██╔══╝     ██║   
    # ╚██████╔╝███████╗   ██║       ██████║      ███████║███████╗   ██║   
    #  ╚═════╝ ╚══════╝   ╚═╝       ╚═════╝      ╚══════╝╚══════╝   ╚═╝   
                                                                        
    def setHand(self,dict:dict):    
        self.hand = dict
    def getHand(self)->dict:        
        return self.hand
    def setBoard(self,board:list):  
        self.board = board
    def getBoard(self)->list:       
        return self.board
    def setDraw(self,tile:string):  
        self.draw = tile
    def getDraw(self)->string:      
        return self.draw
    def getSQ(self)->int:
        return self.sq
    
    
    def getFullHand(self) -> dict:
        fullHand = copy.deepcopy(self.hand)
        for group in self.openMelds:
            for tile in group:
                fullHand[tile] = fullHand.get(tile,0) + 1
        fullHand[self.draw] = fullHand.get(self.draw,0) + 1
        
        
        
        
        
        
