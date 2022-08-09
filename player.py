import copy
import string

class Player():
    def __init__(self):
        self.hand = dict() #key: tileType, value: number of tile
        self.openMelds = list() #List of tuples that represent groups
        self.board = list()
        self.groups = list()
        # self.handgroups = list()
        
        self.ankan = 0
        self.winningTiles = set()
        self.isRichi = False
        self.isDoublerichi = False
        
        self.draw = ""
        self.wind = "E"
        self.sq = 0 #手切次数

    def add(self,tile):
        self.hand[tile] = self.hand.get(tile,0) + 1
    def discard(self, tile):
        # if(tile not in self.hand.keys()):
        #     return False
        if(tile != self.draw):
            self.sq += 1
        self.hand[tile] = self.hand.get(tile,0) - 1
        self.hand = {k:v for k,v in self.hand.items() if v!=0}
        self.board.append(tile) 

        return True
    
    def isLegal(self,dict):
        for v in dict.values():
            if v < 0:
                return False
        return True

    @staticmethod
    def getTileGroup(tile:string): #TODO: no need to go back? if s1 include (s2,s3), then s3 doesn't need to check(s1,s2)
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
        
    # def dfsSearchGroup(self,dict):
    #     if(not self.isLegal(dict)): return False
    #     if(sum(dict.values())==2): #when only 2 tiles left, it should be a two of a kind
    #         return len(dict.keys())==1
    #     else:
    #         tile = ""
    #         for t in dict.keys():
    #             tile = t
    #             old = copy.deepcopy(dict)
    #             for group in Player.getGroup(tile):
    #                 dict[tile] = dict.get(tile,0)-1
    #                 dict[group[0]] = dict.get(group[0],0)-1
    #                 dict[group[1]] = dict.get(group[1],0)-1
    #                 dict = {k:v for k,v in dict.items() if v!=0} # clear zeros so the next first tile is valid
    #                 if(self.dfsSearchGroup(dict)):
    #                     return True
    #                 dict = copy.deepcopy(old)
    #         return False
    def dfsSearchGroup(self,dict:dict,groups:list):
        dict = copy.deepcopy(dict)
        if(sum(dict.values())==2): #when only 2 tiles left, it should be a two of a kind
            if(len(dict.keys())==1):
                for key in dict.keys():
                    groups.append((key,key)) #tuple, no aliasing
                return True,groups
            else:
                False,[]
        else:
            tile = ""
            for t in dict.keys():
                tile = t
                old = copy.deepcopy(dict)
                for group in Player.getTileGroup(tile):
                    dict[tile] = dict.get(tile,0)-1
                    dict[group[0]] = dict.get(group[0],0)-1
                    dict[group[1]] = dict.get(group[1],0)-1
                    dict = {k:v for k,v in dict.items() if v!=0} # clear zeros so the next first tile is valid
                    if(not self.isLegal(dict)):
                        dict = copy.deepcopy(old)
                        # return False,[]
                    else:
                        groups.append((tile,group[0],group[1]))
                        ans = self.dfsSearchGroup(dict,groups)
                        if(ans[0]): 
                            # self.groups.append(ans[1])
                            return True,ans[1]
                        else:
                            return False,[]
                    # return False,[]
               
    def checkWin(self, draw = None):# put this in game.py?
        if draw == None:
            draw = self.draw
        hand = copy.deepcopy(self.hand)
        #add the drawn tile
        hand[draw] = hand.get(draw,0)+1
        ans,groups = self.dfsSearchGroup(hand,list())
        if(not ans): return False
        else:
            self.handgroups = groups
        #Finished checking basic pattern, now check yaku
        
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
    def getOpenMelds(self)->list:
        return self.openMelds
    def setOpenMelds(self,openMelds):
        self.openMelds = openMelds
    def getGroups(self)->list:
        return self.getHandGroups()+self.openMelds
    def getHandGroups(self):
        ans = self.dfsSearchGroup(self.getHand(),list())
        if(ans[0]):
            return ans[1]
        else:
            return []
    def getAnkan(self):
        return self.ankan
    def getWind(self):
        return self.wind
    def setWind(self,wind):
        self.wind = wind
    
    def getFullHand(self) -> dict:
        fullHand = copy.deepcopy(self.hand)
        for group in self.openMelds:
            for tile in group:
                fullHand[tile] = fullHand.get(tile,0) + 1
        if(self.draw!=''):
            fullHand[self.draw] = fullHand.get(self.draw,0) + 1
        return fullHand
    def getRichi(self):
        return self.isRichi, self.isDoublerichi  
    def setWinningTile(self, tiles:list):
        self.winningTiles = tiles
    def getWinningTile(self):
        return self.winningTiles
if __name__ == '__main__':      
    p = Player()
    h = {
        "s1":2,
        "s2":2,
        "s3":2,
        "s4":2,
        "W":3
        
    }
    melds = [('rd','rd','rd')]
    p.setHand(h)
    p.setOpenMelds(melds)

    print(p.dfsSearchGroup(h,list()))
        
