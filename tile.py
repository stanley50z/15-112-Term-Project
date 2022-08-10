class tile_constants():
    OneNineTiles = {'s1','s9','p1','p9','m1','m9'} #清老头牌
    DragonTiles = {'rd','wd','gd'} #三元牌
    WindTiles = {'W','S','E','N'} #风牌
    WordTiles = DragonTiles.union(WindTiles) #字牌
    TerminalTiles = OneNineTiles.union(WordTiles) #幺九牌
    AllGreenTiles = {'s2','s3','s4','s6','s8','gd'} #绿一色牌
    AllTiles = {'s1','s2','s3','s4','s5','s6','s7','s8','s9',
                'm1','m2','m3','m4','m5','m6','m7','m8','m9',
                'p1','p2','p3','p4','p5','p6','p7','p8','p9',
                'E','S','W','N','rd','gd','wd'}