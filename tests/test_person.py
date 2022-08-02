from player import Player
p = Player()
h = {
    "s1":2,
    "s2":2,
    "s3":2,
    "s5":1,
    "W":3
    
}
p.setHand(h)
print(p.checkWin(draw="s5"))