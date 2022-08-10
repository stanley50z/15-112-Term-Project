import sys, copy
sys.path.insert(0, '')
from TermProject.tile import tile_constants
def isHoniso(fullhand):
    # check if the hand has word tiles(we don't want both chiniso and honiso to be true)
    WordTiles = []
    for tile in tile_constants.WordTiles:
        if tile in fullhand.keys():
            WordTiles.append(tile)
    if len(WordTiles)==0: return False
    # remove word tiles
    fullhand = copy.deepcopy(fullhand)
    for tile in WordTiles:
        fullhand.pop(tile)
    # the rest should be true for chiniso  
    type = ""
    for tile in fullhand.keys():
        if(type == ""):
            type = tile[0]
        else:
            if(tile[0] != type):
                return False
    return True


if __name__ == '__main__':
    d = {
        "s1":1,
        "s2":1,
        "s3":1,
        "s4":2,
        "s5":2,
        "s6":2,
        "s7":1,
        "s8":1,
        "s9":1,
        "rd":2
    }

    print(isHoniso(d))