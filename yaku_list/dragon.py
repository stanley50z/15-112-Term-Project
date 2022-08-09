

# yes, this may seem repetitive, but since these are treated seperatedly when counting yakus
# just like kokushi, these are under the same kind of yaku but counted seperately
def isReddragon(fullhand): 
    return 'rd' in fullhand.keys() and fullhand['rd']>=3

def isGreendragon(fullhand): 
    return 'gd' in fullhand.keys() and fullhand['gd']>=3

def isWhitedragon(fullhand): 
    return 'wd' in fullhand.keys() and fullhand['wd']>=3
