

from cmu_112_graphics import *


def playMahjong():
    runApp(width=1920,height=1080)

def appStarted(app):
    pass

def redrawAll(app,canvas):
    canvas.create_text(500,500,text = "🀝", font = ("Segoe UI", 150), fill = "red")







#################################################
# main
#################################################

def main():
    playMahjong()

if __name__ == '__main__':
    main()