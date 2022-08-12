import sys
import math, decimal

sys.path.insert(0, '')
from TermProject.player import Player
from TermProject.tile import tile_constants
from TermProject.yaku_list import (kokushi, #limits
                                   chiniso, #6 han
                                   junchantai_yaochu, honiso, ryanpeiko, # 3 han
                                   chitoitsu,sanshoku,sankantsu,toitoiho,sananko,shosangen,honchantai_yaochu,ikkitsuukan, # 2 han
                                   ipeiko, richi, tanyaochu,pinfu,wind,dragon, tsumo # 1 han
                                   )
from TermProject.Fu_util import fu_melds,fu_waits
MANGAN = 4000
# BASICTABLE = {
#     1: {
#         30:1300,        40:1600,
#         50:1300,        60:2000,
#         70:2300,        80:2600,
#         90:2900,        100:3200,
#         110:3600
#         },
#     2: {
#         25:1600,        30:2000,
#         40:2600,        50:3200,
#         60:3900,        70:4500,
#         80:5200,        90:5800,
#         100:6400,        110:7100
#         },
#     3: {
#         25:3200,        30:2000,
#         40:5200,        50:3200,
#         60:7700,        70:4500,
#         80:5200,        90:5800,
#         100:6400,        110:7100
#         },
#     4: {}
# }

# from player import Player
# from yaku_list import (chitoitsu,tsumo,kokushi)
class ScoreCounter():
    def __init__(self, player:Player):
        self.draw = ""

        self.hand = player.getHand()
        self.board = player.getBoard()
        self.draw = player.getDraw()
        self.openMelds = player.getOpenMelds()
        self.fullhand = player.getFullHand()
        self.handgroups = player.getHandGroups()
        self.groups = player.getGroups()
        self.noOpenMelds = self.openMelds==[] #是否门清
        self.ankan = player.getAnkan()
        self.isRichi,self.isDoublerichi = player.getRichi()
        self.wind = player.getWind()
        self.dealerWind = 'E'
        self.winningTile = player.getWinningTile()
        
        self.dora = ''
        self.han = 0 #役数
        self.fu = 0 #符数
        self.point = 0
        self.yaku = set() #役种，因为可以同时达成多个役种，所以是set而非单个变量
    

    
    def checkYakus(self, winningTile):
        # double-limit
        if kokushi.isKokushi13(self.hand):
            self.han += 26
            self.yaku.add('kokushi13')
        # limit
        if kokushi.isKokushi(self.fullhand):
            self.han += 13
            self.yaku.add('kokushi')
        # TODO: all Yakumans
        # since all Yakumans are super rare, there's no point to complete them due to time constraints
        
        # 6 han yaku: chiniso清一色
        if(chiniso.isChiniso(self.fullhand)):
            self.han += 6
            if not self.noOpenMelds: #副露减1番
                self.han -= 1
            self.yaku.add('chiniso')    
        # 3 han yakus: junchantai yaochu纯全幺九, honiso混一色, ryanpeiko二杯口
        if(self.noOpenMelds): # no open melds is required               #ryanpeiko二杯口，门清限定
            if(ryanpeiko.isRyanpeiko(self.fullhand)):
                self.han += 3
                self.yaku.add('ryanpeiko')
        if(junchantai_yaochu.isJunchantai_yaochu(self.groups)):         #纯全幺九，副露减1番
            self.han += 3
            if not self.noOpenMelds: #deduct 1 han if there's any open meld
                self.han -= 1
            self.yaku.add('junchantai_yaochu')

        if(honiso.isHoniso(self.fullhand)):                             #混一色，副露减1番   
            self.han += 3
            if not self.noOpenMelds:
                self.han -= 1
            self.yaku.add('honiso')
                
        # 2 han yakus:      chitoitsu七对子，           sanshoku douko/doujun三色同刻/顺
                    #       sankantsu三刻子，           toitoiho对对和
                    #       sananko三暗刻，             shosangen小三元
                    #       honchantai_yaochu混全幺九， ikkitsuukan一气通贯
                    #       double_richi双立直
        if(chitoitsu.isChitoitsu(self.fullhand)):                       #七对子，符数固定25
            self.han += 2
            self.yaku.add('chitoitsu')
        if(sanshoku.isDouko(self.fullhand)):                            #三色同刻
            self.han += 2
            self.yaku.add('sanshoku_douko')
        if(sanshoku.isDoujun(self.fullhand)):                           #三色同顺，副露-1
            self.han += 2
            if not self.noOpenMelds:
                self.han -= 1
            self.yaku.add('sanshoku_doujin')
        if(sankantsu.isSankantsu(self.openMelds)):                      #三杠子
            self.han += 2
            self.yaku.add('sankantsu')
        if(toitoiho.isToitoiho(self.groups)):                           #对对和
            self.han += 2
            self.yaku.add('toitoiho')
        if(sananko.isSananko(self.handgroups,self.ankan)):              #三暗刻
            self.han += 2
            self.yaku.add('sananko')
        if(shosangen.isShosangan(self.fullhand)):                       #小三元
            self.han += 2
            self.yaku.add('shosangen')
        if(honchantai_yaochu.isHonchantai_yaochu(self.groups)):         #混全幺九，副露-1
            self.han += 2
            if not self.noOpenMelds:
                self.han -= 1
            self.yaku.add('honchantai_yaochu')
        if(ikkitsuukan.isIkkitsuukan(self.fullhand)):                   #一气通贯，副露-1
            self.han += 2
            if not self.noOpenMelds:
                self.han -= 1
            self.yaku.add('ikkitsuukan') 
        if(richi.isDoublerichi(self.isDoublerichi)):
            self.han += 2
            self.yaku.add('double_richi') 
        
        # 1 han yakus:
        if(ipeiko.isIpeiko(self.fullhand) and self.noOpenMelds):        #一杯口
            self.han += 1
            self.yaku.add('ipeiko')
        if(richi.isRichi(self.isRichi)):                                #立直
            self.han += 1
            self.yaku.add('richi') 
        if(tanyaochu.isTanyaochu(self.fullhand)):                       #断幺九
            self.han += 1
            self.yaku.add('tanyaochu')
        if(tsumo.isTsumo(self.openMelds,self.draw)):                    #自摸，门清限定
            self.han += 1
            self.yaku.add('tsumo')
        # if(wind.isDealerWind(self.fullhand,game.getDealerwind())):      #场风
        #     self.han += 1
        #     self.yaku.add('dealer_wind')
        if(wind.isSelfWind(self.fullhand,self.wind)):                   #自风
            self.han += 1
            self.yaku.add('self_wind')
        if(dragon.isReddragon(self.fullhand)):                          #中
            self.han += 1
            self.yaku.add('red_dragon')
        if(dragon.isGreendragon(self.fullhand)):                        #发
            self.han += 1
            self.yaku.add('green_dragon')
        if(dragon.isWhitedragon(self.fullhand)):                        #白
            self.han += 1
            self.yaku.add('white_dragon')
        if(pinfu.isPinfu(self.groups,winningTile,self.wind)):           #平和，门清限定
            if(self.noOpenMelds):
                self.han += 1
                self.yaku.add('pinfu')
                
        if('chitoitsu' in self.yaku):
            if('ryanpeiko' in self.yaku):
                self.yaku.remove('chitoitsu')
                self.han -= 2
            if('ipeiko' in self.yaku):
                self.yaku.remove('ipeiko')
                self.han -= 1
        # TODO: haitei海底捞月，houtei河底捞鱼，rinchan岭上开花，chankan抢杠
        # these are all very luck-base yakus, and adding them won't make a big difference
        # that being said, tsumo is also luck-based, but since it's way more common and involves with other game mechanics, so I included it
        # I will add those yakus later to make the algorithm more accurate
        
    def checkDora(self):
        for tile in self.fullhand.keys():
            if tile == self.dora:
                self.han += self.fullhand[tile]
    def countFu(self):
        fu = 20    # a winning hand gets 20 fu automatically (futei)
        if(self.noOpenMelds and self.winningTile!=self.draw):
            fu += 10 # if ron with no open melds, add 10
        for group in self.handgroups:
            fu += fu_melds(group,True,self.wind,self.dealerWind)
        for group in self.openMelds:
            fu += fu_melds(group,False,self.wind,self.dealerWind)
        fu += self.ankan*8
        self.fu += fu_waits('',list())
        if(self.winningTile == self.draw):
            fu += 2 #TODO: pinfu exception
        if('chitoitsu' in self.yaku):
            return 25
        else:
            fu = math.ceil(fu/10) * 10  # fu always round UP to tens, except for chitoitsu, which is fixed at 25
            return fu
    
    def roundHalfUp(self,d): #helper-fn
        # Round to nearest with ties going away from zero.
        rounding = decimal.ROUND_HALF_UP
        # See other rounding options here:
        # https://docs.python.org/3/library/decimal.html#rounding-modes
        return int(decimal.Decimal(d).to_integral_value(rounding=rounding))
    
    # for this part of calculation, see here https://en.wikipedia.org/wiki/Japanese_mahjong_scoring_rules#Calculating_basic_points
    def ScoreBasic(self):
        han = self.han
        fu = self.fu
        basicPoints = fu * math.pow(2,2+han) * 2
        basicPoints = self.roundHalfUp(basicPoints/100) * 100  # round up to the nearest 100
        self.point = basicPoints
    
    # for this part of calculation, see here https://en.wikipedia.org/wiki/Japanese_mahjong_scoring_rules#Mangan
    def ScoreMangan(self):
        h = self.han
        if(h<=5): # a hand with less than 5 han can be counted as Mangan if there are enough 'fu' points
            self.point = MANGAN
        elif h in range(6,8):
            self.point = int(1.5*MANGAN)
        elif h in range(8,11):
            self.point = int(2*MANGAN)
        elif h in range(11,13):
            self.point = int(3*MANGAN)
        elif h >= 13:
            self.point = int(4*MANGAN*(h//13))

    # the steps can be explained here https://en.wikipedia.org/wiki/Japanese_mahjong_scoring_rules
    # 1. Check all yakus(winning patterns) and count 'han'
    # 2. If 'han' is big enough, skip to no.5
    # 3. Count 'fu', if 'han' and 'fu' combined is big enough, skip to no.5
    # 4. Calculate basic points with 'han' and 'fu'
    # 5. Multiply for dealer, tsumo, etc.
    def getScore(self,dora,winningTile=None):
        self.dora = dora
        self.checkYakus(winningTile)
        if(self.han == 0): return 0
        self.checkDora()    # Dora counts only when there's at least one yaku already
        if(self.han<5):
            self.fu = self.countFu()
            self.ScoreBasic()
        else:
            self.ScoreMangan()
        print(self.yaku)
        print(self.han)
        print(self.fu)
        if(self.wind == 'E'):
            return self.point*3 
        else:
            return self.point*2
    def getYaku(self):
        return self.yaku
# TODO: Organize hand into groups (may have more than one ways to organize)
# TODO: Catogrize group for detecting yaku(chi,pon,kan,etc)
# TODO: Detect every kind of yaku (some yaku may not happen at the same time, ex:两杯口和七对子)

if __name__ == '__main__':
    p = Player("player")
    hand = {
        "s1":2,
        "s2":1,
        "s3":1,
        "s4":4,
        "s5":1,
        "s6":1,
        "s7":1
        
    }
    openMelds = [('rd','rd','rd')]
    p.setHand(hand)
    p.setOpenMelds(openMelds)
    score = ScoreCounter(p)
    print(score.getScore('wd'))
    print(score.yaku)
    print(score.han)
    print(score.fu)
