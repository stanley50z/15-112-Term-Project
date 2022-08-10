import sys
sys.path.insert(0, '')
from TermProject.tile import tile_constants

def isKokushi(fullhand): #国士无双
    for onenine in tile_constants.OneNineTiles:
        if onenine not in fullhand.keys():
            return False
    return True
def isKokushi13(hand): #国士无双13面
    for onenine in tile_constants.OneNineTiles:
        if onenine not in hand.keys():
            return False

# d = {
#     "s1":2,
#     "s9":1,
#     "m1":1,
#     "m9":1,
#     "p1":1,
#     "p9":1,
#     "rd":1,
#     "gd":1,
#     "wd":1,
#     "W":1,
#     "E":1,
#     "N":1,
#     "S":1,
# }
# print(isKokushi(d))