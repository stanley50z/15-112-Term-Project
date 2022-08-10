import sys
sys.path.insert(0, '')
from TermProject.player import Player
from TermProject.game import game

def isToi(group):
    t = ""
    for tile in group:
        if(t == ""): t = tile
        if(tile != t): return False
    return True

# see here for details https://en.wikipedia.org/wiki/Japanese_mahjong_scoring_rules#Fu_of_melds
def fu_melds(group,isHand,selfWind,dealerWind):
    fu = 0
    if(not isToi(group)): return fu
    if len(group)==2:
        if group[0] in game.DragonTiles or group[0] == selfWind or group[0] == dealerWind: 
            fu +=2                                      # if it's dragon, selfwind, dealerwind, add 2  
        if selfWind == dealerWind:                      # if the pair is dealer's wind and dealer wins, add another 2
            fu += 2
        return fu
    elif len(group)==3:
        fu = 2
    elif len(group)==4:
        fu = 8
    if(isHand): fu *= 2                                 # for pon and kan, if it's closed, multiply by 2
    if(group[0] in game.WordTiles):  fu*= 2             # if the group is honor tiles(word tiles), multiply by 2 again
    return fu
# see here https://en.wikipedia.org/wiki/Japanese_mahjong_scoring_rules#Fu_of_waits
def fu_waits(winningTile, groups):
    # since this part requires many extra coding but merely 2 fu max, I won't do this part
    return 0