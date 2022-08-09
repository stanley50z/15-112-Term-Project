

def isDoujun(fullhand:dict): #三色同顺
    for i in range(2,9):
        found = True
        for type in ['s','m','p']:
            if not ((type+str(i-1) in fullhand.keys()) and (type+str(i) in fullhand.keys()) and (type+str(i+1) in fullhand.keys())):
                found = False
        if(found): return True
    return False

def isDouko(fullhand:dict): #三色同刻
    for i in range(1,10):
        found = True
        for type in ['s','m','p']:
            if not type+str(i) in fullhand.keys():
                found = False
            else:
                if(fullhand[type+str(i)]<3):
                    found = False
        if(found): return True
    return False
if __name__ == '__main__':
    d = {
        "s1":2,
        "s2":2,
        "s3":2,
        "s5":2,
        "W":3
    }

    print(isDoujun(d))