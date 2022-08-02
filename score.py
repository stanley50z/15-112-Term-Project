from player import Player
class ScoreCounter(Player):
    def __init__(self):
        self.noOpenMelds = True #是否门清
        self.han = 0 #役数
        self.fu = 0 #符数
        self.draw = ""
        self.yaku = list() #役种，因为可以同时达成多个役种，所以是list而非单个变量
        

# Note: Due to time constraint, I will not complete this part for TP
#       Plus, for a deck tracker, this doesn't matter that much
# TODO: Organize hand into groups (may have more than one ways to organize)
# TODO: Catogrize group for detecting yaku(chi,pon,)
# TODO: Detect every kind of yaku (some yaku may not happen at the same time, ex:两杯口和七对子)

