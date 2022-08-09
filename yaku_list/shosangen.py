import sys
sys.path.insert(0, '')
from TermProject.game import game

def isShosangan(fullhand):
    istwo = False
    for tile in game.DragonTiles:
        if tile not in fullhand.keys():
            return False
        else:
            if(fullhand[tile]==2):
                istwo = True
    return istwo