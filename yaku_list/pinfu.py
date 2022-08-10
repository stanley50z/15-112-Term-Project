import sys
sys.path.insert(0, '')
from TermProject.tile import tile_constants
from TermProject.yaku_list.toitoiho import isToi

def isPinfu(groups, draw, selfwind):
    found = False
    if draw in tile_constants.WordTiles: return False                                 # the draw must not be a word tile
    for group in groups:
        if(len(group)==2):                                                  # the pair must not be a dragon tile or self wind
            for tile in group:
                if tile == selfwind or tile in tile_constants.DragonTiles:
                    return False
        elif(draw in group):
            type = draw[0]
            num = int(draw[1])
            if(not type+str(num-1) in group) == (type+str(num+1) in group): # xor, the drawn tile must be next to the two neighbor tiles
                found = True
        else:
            if isToi(group): return False                                   # there must be no triplets or squads in pinfu
    return found

if __name__ == '__main__':
    d = [('s1', 's2', 's3'), ('s1', 's2', 's3'), ('s7', 's8', 's9'),('p7','p7','p7'), ('W', 'W')] #has triplet
    print(isPinfu(d,'s1','E'))

    d = [('s1', 's2', 's3'), ('s1', 's2', 's3'), ('s7', 's8', 's9'),('p2','p3','p4'), ('W', 'W')] #drawn in the middle
    print(isPinfu(d,'s2','E'))
    
    d = [('s1', 's2', 's3'), ('s1', 's2', 's3'), ('s7', 's8', 's9'),('p2','p3','p4'), ('E', 'E')] #has self wind
    print(isPinfu(d,'s1','E'))

    d = [('s1', 's2', 's3'), ('s1', 's2', 's3'), ('s7', 's8', 's9'),('p2','p3','p4'), ('W', 'W')] #finally pass
    print(isPinfu(d,'s1','E'))