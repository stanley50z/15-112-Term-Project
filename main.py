from cmu_112_graphics import *
from game import game
from tile import tile_constants

def playMahjong():
    runApp(width=640,height=1120)

def appStarted(app):
    app.input = ''
    app.target = None
    
    app.midx = app.width/2
    app.midy = app.height/2
    app.cx = 0
    app.cy = 0
    app.game = game()
    app.msg = ''
    app.tiles = list()
    app.buttonBounds = dict()
    app.playerBounds = dict()
    app.tile = ''
    app.tilex = 85
    app.tiley = 115
    app.action = ''
    app.isAction = False
    app.isDrawing = True
    
    setTiles(app)
    setButtonBounds(app)
    setPlayerBounds(app)
    pass

def setTiles(app):
    app.tiles = [ # come on, this is a brain dead way to do this, and I am brain dead at this moment.
        ['s1','s2','s3','s4','s5'],
        ['s5','s6','s7','s8','s9'],
        ['p1','p2','p3','p4','p5'],
        ['p5','p6','p7','p8','p9'],
        ['E','S','W','N','rd'],
        ['gd','wd','m1','m9']
    ]

def setButtonBounds(app):
    # nothing particular with the specific numbers
    # I copy-pasted them from my .ai design file
    app.buttonBounds = {
        '-a': (535,940,535+app.tilex,940+app.tiley),
        'pei':(33,80, 33+168, 80+92),
        'pon':(233,80, 233+168, 80+92),
        'kan':(433,80, 433+168, 80+92)
    }

def setPlayerBounds(app):
    app.playerBounds = {
        'player':(233, 450, 233+168, 450+92)
    }
    playerwind = app.game.getPlayers()[0].getWind()
    if(playerwind == 'E'):
        app.playerBounds['p1'] = (433,350, 433+168, 350+92)
        app.playerBounds['p2'] = (233,250, 233+168, 250+92)
    elif(playerwind == 'S'):
        app.playerBounds['p1'] = (433,350, 433+168, 350+92)
        app.playerBounds['p2'] = (33,350, 33+168, 350+92)
    elif(playerwind == 'W'):
        app.playerBounds['p1'] = (233,250, 233+168, 250+92)
        app.playerBounds['p2'] = (33,350, 33+168, 350+92)
    pass

def keyPressed(app,event):
    key = event.key
    if(key == 'Backspace'):
        app.input = app.input[:-1]
    else:
        app.input = app.input + key    

def reset(app):
    app.action = ''
    app.tile = ''
    app.target = None

def mousePressed(app,event):
    app.cx = event.x
    app.cy = event.y
    if(app.isAction):
        getActions(app)
        getPlayer(app)
    else:
        getTiles(app)
    # printInfo(app)
    doAction(app)
    app.game.printBoard()
    
def getTiles(app):
    x = app.cx
    y = app.cy
    col = (x-20)//125
    row = (y-65)//175
    # print(str(row)+','+str(col))
    if(row < 0 or row > 5): return True
    if(col < 0 or col > 4): return True
    bx0,by0,bx1,by1 = app.buttonBounds['-a']
    if(x>bx0 and x<bx1 and y>by0 and y<by1):    # check if clicked on action button
        app.action = '-a'
        app.isAction = not app.isAction
        return False
    else:
        if((x-20)%125>85 or (y-65)%175>115): return True# check if the click is on the gap
        app.tile = app.tiles[row][col]
        return False

def getActions(app):
    x, y = app.cx, app.cy
    for action in app.buttonBounds.keys():
        bx0,by0,bx1,by1 = app.buttonBounds[action]
        if(x>bx0 and x<bx1 and y>by0 and y<by1):
            app.action = action
            if action == '-a': 
                app.isAction = not app.isAction
            return False
    return True
                
def doAction(app):
    if app.action == '-a': 
        reset(app)
        return
    cp = app.game.getCurrentPlayer()
    
    if app.isAction:
        action = app.action
        # if action == '-a':
        #     app.isAction = not app.isAction
        #     return doAnalyze(app)
        if action == 'pei':
            app.isAction = False
            return app.game.pei()
        elif action == 'pon':
            if(app.target == None): return
            app.isAction = False
            if(app.target == 0): app.isDrawing = False
            return app.game.pon(app.target)

        elif action == 'kan':
            if(app.target == None): return
            app.isAction = False
            app.game.kan(app.target)
            if(app.target == 0): app.isDrawing = True
            # return app.game.discardTile(app.tile)
    else:
        tile = app.tile
        if app.isDrawing and cp == 0:
            app.game.drawTile(tile)
            app.isDrawing = False
        else:
            app.game.discardTile(tile)
            app.isDrawing = True

    reset(app)

def getPlayer(app):
    x = app.cx
    y = app.cy
    for player in app.playerBounds.keys():
        bx0,by0,bx1,by1 = app.playerBounds[player]
        if(x>bx0 and x<bx1 and y>by0 and y<by1):
            if(player == 'player'):
                app.target = 0
            elif(player == 'p1'):
                app.target = 1
            elif(player == 'p2'):
                app.target = 2
        return False
    return True
    # print(app.target)


def doAnalyze(app):
    # print(app.game.getAnalysis())
    return False



def playGame(self, start = False):
    # if not (start or self.coldStart): return
    if self.coldStart and (not start):
            return
    if not self.coldStart:
        self.getStart()
    while True:
        self.printBoard()
        cp = self.currentPlayer
        if(cp==0):
            draw = self.getLegalInput("Enter your draw: \n")
            if draw != '':
                self.players[cp].add(draw)
        while(self.doAction()):
                pass
# 535 940 width 85+40 height 115+60       margin 20,65 
def drawTileBlocks(app,canvas):
    text = "🀐 🀑 🀒 🀓 🀔\n🀔 🀕 🀖 🀗 🀘\n🀙 🀚 🀛 🀜 🀝\n🀝 🀞 🀟 🀠 🀡\n🀀 🀁 🀂 🀃 🀄\n🀅 🀆 🀇 🀏 "
    font = ("Segoe UI", 100)
    canvas.create_text(app.midx,30,
                       anchor = 'n',
                       text = text,
                       font = font)
    for row in range(6):
        for col in range(5):
            if row == 5 and col == 4:return
            tile = app.tiles[row][col]
            text = app.game.getDeck().get(tile,0)
            canvas.create_text(20+42.5+col*128,65+120+row*175,
                                anchor = 'n',
                                text = text,
                                font = ("Segoe UI", 20))
    
def drawButtons(app,canvas):
    for action in app.buttonBounds.keys():
        if action == '-a': continue
        bx0,by0,bx1,by1 = app.buttonBounds[action]
        canvas.create_rectangle(bx0,by0,bx1,by1,fill='white',width=2)
        canvas.create_text((bx0+bx1)/2,(by0+by1)/2,text = action,font=("Segoe UI", 50))

def drawPlayers(app,canvas):
    for player in app.playerBounds.keys():
        bx0,by0,bx1,by1 = app.playerBounds[player]
        canvas.create_rectangle(bx0,by0,bx1,by1,fill='white',width=2)
        canvas.create_text((bx0+bx1)/2,(by0+by1)/2,text = player,font=("Segoe UI", 50))

def drawActionButton(app,canvas):
    bx0,by0,bx1,by1 = app.buttonBounds['-a']
    canvas.create_rectangle(bx0,by0,bx1,by1,fill = 'pink')
    canvas.create_text((bx0+bx1)/2,(by0+by1)/2,text = 'Action',font=("Segoe UI", 20))

def printMessage(app,canvas):
    cp = app.game.getCurrentPlayer()
    msg = ''
    if(app.isAction):
        msg = "Press the Action:"
    else:
        if(app.isDrawing and cp == 0):
            msg = "Press the drawn tile:"
        else:
            msg = f"Press the discarded tile from {cp}"
    canvas.create_text(app.midx,20,
                       text = msg,
                       font = ("Segoe UI", 10),
                       anchor='n')

def printAnalysis(app,canvas):
    analysis = app.game.getAnalysis()
    msg = str(analysis[0])+'\n'+str(analysis[1])
    canvas.create_text(50,650,
                       text = msg,
                       font = ("Segoe UI", 20),
                       anchor='n')

def printMouse(app,canvas):
    text = str(app.cx)+', '+str(app.cy)
    if(app.isAction):
        canvas.create_text(app.cx,app.cy,text = text+app.action)
    else:
        canvas.create_text(app.cx,app.cy,text = text+app.tile)
    
def printInfo(app):
    print(f"action: {app.action}")
    print(f"tile: {app.tile}")
    print(f"target: {app.target}")
    print(f"isAction: {app.isAction}")
    
def redrawAll(app,canvas):
    if app.isAction:
        drawButtons(app,canvas)
        drawPlayers(app,canvas)
        printAnalysis(app,canvas)
    else:
        drawTileBlocks(app,canvas)
    drawActionButton(app,canvas)
    printMessage(app,canvas)
    printMouse(app,canvas)
    
    pass


def isLegalInput(app):
    actionList = ['-a','deck','chi','pon','kan']
    if app.input in tile_constants.AllTiles or app.input in actionList:
        return True
    else:
        return False


    




#################################################
# main
#################################################

def main():
    playMahjong()

if __name__ == '__main__':
    main()