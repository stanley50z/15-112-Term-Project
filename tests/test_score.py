import sys
sys.path.insert(0, '')

from TermProject.player import Player
from TermProject.score import ScoreCounter

# from ..player import Player
# from ..score import ScoreCounter
# from .. import player
# from .. import score
p = Player()
h = {
    "s1":2,
    "s2":2,
    "s3":2,
    "s5":2,
    "W":2,
    'm9':2,
    's6':1
    
}
melds = []
p.setHand(h)
p.setOpenMelds(melds)
p.setDraw('s6')
score = ScoreCounter(p)
print(score.getScore())
