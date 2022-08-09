import sys
sys.path.insert(0, '')
from TermProject.game import game

def isHunroto(fullhand):
    for tile in fullhand.keys():
        if not (tile in game.OneNineTiles or tile in game.WordTiles):
            return False
    return True    
    