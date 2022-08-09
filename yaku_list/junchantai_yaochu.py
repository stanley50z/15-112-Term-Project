import sys
sys.path.insert(0, '')
from TermProject.game import game

def isJunchantai_yaochu(groups):
    for group in groups:
        isOneNine = False
        for tile in (group):
            if tile in game.WordTiles:
                return False
            if(tile[1]=='1' or tile[1]=='9'):
                isOneNine = True
        if not isOneNine: return False
    return True

# d = [('s1', 's2', 's3'), ('s1', 's2', 's3'), ('s7', 's8', 's9'), ('p2', 'p2')]
# print(isJunchantai_yaochu(d))