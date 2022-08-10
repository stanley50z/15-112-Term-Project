import sys
sys.path.insert(0, '')
from TermProject.tile import tile_constants

def isShosangan(fullhand):
    istwo = False
    for tile in tile_constants.DragonTiles:
        if tile not in fullhand.keys():
            return False
        else:
            if(fullhand[tile]==2):
                istwo = True
    return istwo