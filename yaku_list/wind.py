def isSelfWind(fullhand,selfwind):
    if(selfwind in fullhand.keys() and fullhand[selfwind]>=3):
        return True
    else:
        return False

def isDealerWind(fullhand,dealerwind):
    if(dealerwind in fullhand.keys() and fullhand[dealerwind]>=3):
        return True
    else:
        return False