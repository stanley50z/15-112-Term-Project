from player import Player
class ScoreCounter():
    def __init__(self, player:Player):
        self.noOpenMelds = True #是否门清
        self.draw = ""

        self.hand = player.getHand()
        self.board = player.getBoard()
        self.draw = player.getDraw()


        self.han = 0 #役数
        self.fu = 0 #符数
        self.yaku = list() #役种，因为可以同时达成多个役种，所以是list而非单个变量
        

# TODO: Organize hand into groups (may have more than one ways to organize)
# TODO: Catogrize group for detecting yaku(chi,pon,kan,etc)
# TODO: Detect every kind of yaku (some yaku may not happen at the same time, ex:两杯口和七对子)

