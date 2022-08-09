import sys
sys.path.insert(0, '')
from TermProject.player import Player
from TermProject.game import game
from TermProject.yaku_list import (kokushi, #limits
                                   chiniso, #6 han
                                   junchantai_yaochu, honiso, ryanpeiko, # 3 han
                                   chitoitsu,sanshoku,sankantsu,toitoiho,sananko,shosangen,honchantai_yaochu,ikkitsuukan, # 2 han
                                   ipeiko, richi, tanyaochu,pinfu,wind,dragon, tsumo # 1 han
                                   )
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
        self.winningTile = player.getWinningTile()

        self.han = 0 #役数
        self.fu = 0 #符数
        self.yaku = list() #役种，因为可以同时达成多个役种，所以是list而非单个变量
    

    
    def checkYakus(self, winningTile):
        # double-limit
        if kokushi.isKokushi13(self.hand):
            self.han += 26
            self.yaku.append('kokushi13')
        # limit
        if kokushi.isKokushi(self.fullhand):
            self.han += 13
            self.yaku.append('kokushi')
        # TODO: all Yakumans
        # since all Yakumans are super rare, there's no point to complete them due to time constraints
        
        # 6 han yaku: chiniso清一色
        if(chiniso.isChiniso(self.fullhand)):
            self.han += 6
            if not self.noOpenMelds: #副露减1番
                self.han -= 1
                
        # 3 han yakus: junchantai yaochu纯全幺九, honiso混一色, ryanpeiko二杯口
        if(self.noOpenMelds): # no open melds is required               #ryanpeiko二杯口，门清限定
            if(ryanpeiko.isRyanpeiko(self.fullhand)):
                self.han += 3
                self.yaku.append('ryanpeiko')
        if(junchantai_yaochu.isJunchantai_yaochu(self.groups)):         #纯全幺九，副露减1番
            self.han += 3
            if not self.noOpenMelds: #deduct 1 han if there's any open meld
                self.han -= 1
            self.yaku.append('junchantai_yaochu')

        if(honiso.isHoniso(self.fullhand)):                             #混一色，副露减1番   
            self.han += 3
            if not self.noOpenMelds:
                self.han -= 1
            self.yaku.append('honiso')
                
        # 2 han yakus:      chitoitsu七对子，           sanshoku douko/doujun三色同刻/顺
                    #       sankantsu三刻子，           toitoiho对对和
                    #       sananko三暗刻，             shosangen小三元
                    #       honchantai_yaochu混全幺九， ikkitsuukan一气通贯
                    #       double_richi双立直
        if(chitoitsu.isChitoitsu(self.fullhand)):                       #七对子，符数固定25
            self.han += 2
            self.yaku.append('chitoitsu')
            return # Chitoitsu is a special yaku, so no need to check the rest
        if(sanshoku.isDouko(self.fullhand)):                            #三色同刻
            self.han += 2
            self.yaku.append('sanshoku_douko')
        if(sanshoku.isDoujun(self.fullhand)):                           #三色同顺，副露-1
            self.han += 2
            if not self.noOpenMelds:
                self.han -= 1
            self.yaku.append('sanshoku_doujin')
        if(sankantsu.isSankantsu(self.openMelds)):                      #三杠子
            self.han += 2
            self.yaku.append('sankantsu')
        if(toitoiho.isToitoiho(self.groups)):                           #对对和
            self.han += 2
            self.yaku.append('toitoiho')
        if(sananko.isSananko(self.handgroups,self.ankan)):              #三暗刻
            self.han += 2
            self.yaku.append('sananko')
        if(shosangen.isShosangan(self.fullhand)):                       #小三元
            self.han += 2
            self.yaku.append('shosangen')
        if(honchantai_yaochu.isHonchantai_yaochu(self.groups)):         #混全幺九，副露-1
            self.han += 2
            if not self.noOpenMelds:
                self.han -= 1
            self.yaku.append('honchantai_yaochu')
        if(ikkitsuukan.isIkkitsuukan(self.fullhand)):                   #一气通贯，副露-1
            self.han += 2
            if not self.noOpenMelds:
                self.han -= 1
            self.yaku.append('ikkitsuukan') 
        if(richi.isDoublerichi(self.isDoublerichi)):
            self.han += 2
            self.yaku.append('double_richi') 
        
        # 1 han yakus:
        if(ipeiko.isIpeiko(self.fullhand) and self.noOpenMelds):        #一杯口
            self.han += 1
            self.yaku.append('ipeiko')
        if(richi.isRichi(self.isRichi)):                                #立直
            self.han += 1
            self.yaku.append('richi') 
        if(tanyaochu.isTanyaochu(self.fullhand)):                       #断幺九
            self.han += 1
            self.yaku.append('tanyaochu')
        if(tsumo.isTsumo(self.openMelds,self.draw)):                    #自摸，门清限定
            self.han += 1
            self.yaku.append('tsumo')
        # if(wind.isDealerWind(self.fullhand,game.getDealerwind())):      #场风
        #     self.han += 1
        #     self.yaku.append('dealer_wind')
        if(wind.isSelfWind(self.fullhand,self.wind)):                   #自风
            self.han += 1
            self.yaku.append('self_wind')
        if(dragon.isReddragon(self.fullhand)):                          #中
            self.han += 1
            self.yaku.append('red_dragon')
        if(dragon.isGreendragon(self.fullhand)):                        #发
            self.han += 1
            self.yaku.append('green_dragon')
        if(dragon.isWhitedragon(self.fullhand)):                        #白
            self.han += 1
            self.yaku.append('white_dragon')
        if(pinfu.isPinfu(self.groups,winningTile,self.wind)):           #平和，门清限定
            if(self.noOpenMelds):
                self.han += 1
                self.yaku.append('pinfu')
        # TODO: haitei海底捞月，houtei河底捞鱼，rinchan岭上开花，chankan抢杠
        # these are all very luck-base yakus, and adding them won't make a big difference
        # that being said, tsumo is also luck-based, but since it's way more common and involves with other game mechanics, I included it
        # will add those yakus later to make the algorithm more accurate
    def getScore(self,winningTile):
        self.checkYakus(winningTile)
        return self.han*1000
        
# TODO: Organize hand into groups (may have more than one ways to organize)
# TODO: Catogrize group for detecting yaku(chi,pon,kan,etc)
# TODO: Detect every kind of yaku (some yaku may not happen at the same time, ex:两杯口和七对子)

if __name__ == '__main__':
    p = Player()
    hand = {
        "s1":2,
        "s2":2,
        "s3":2,
        "s5":2,
        "W":3
        
    }
    openMelds = [('rd','rd','rd')]
    p.setHand(hand)
    p.setOpenMelds(openMelds)
    score = ScoreCounter(p)
    print(score.getScore(''))
    print(score.yaku)
