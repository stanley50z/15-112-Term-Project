import sys
sys.path.insert(0, '')
from TermProject.tile import tile_constants

def isHunroto(fullhand):
    for tile in fullhand.keys():
        if not (tile in tile_constants.OneNineTiles or tile in tile_constants.WordTiles):
            return False
    return True    
    