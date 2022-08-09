import sys
sys.path.insert(0, '')
from TermProject.game import game
def isTanyaochu(fullhand):
    for tile in fullhand.keys():
        if tile in game.TerminalTiles:
            return False
    return True

if __name__ == '__main__':
    d = {
        "s2":3,
        "p2":3,
        "m2":2,
        "m3":1,
        "m4":1,
        "m5":1,
        "m8":3,
    }
    print(isTanyaochu(d))