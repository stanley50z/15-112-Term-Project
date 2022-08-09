import sys, copy
sys.path.insert(0, '')
from TermProject.game import game

def isHonchantai_yaochu(groups):
    for group in groups:
        isOneNineorWord = False
        for tile in (group):
            # short circuit, otherwise, wind tiles don't have a second digit
            if(tile in game.WordTiles or tile[1]=='1' or tile[1]=='9' ):
                isOneNineorWord = True
        if not isOneNineorWord: return False
    return True

if __name__ == '__main__':
    d = [('s1', 's2', 's3'), ('s1', 's2', 's3'), ('s7', 's8', 's9'),('rd','rd','rd'), ('W', 'W')]
    print(isHonchantai_yaochu(d))