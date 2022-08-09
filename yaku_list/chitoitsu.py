def isChitoitsu(fullhand:dict): #七对子
    for tile in fullhand.keys():
        if(fullhand[tile]!=2):
            return False
    return True

if __name__ == '__main__':
    d = {
        "rd":2,
        "s3":2,
        "s4":2,
        "s5":2,
        "p4":3,
        "p5":3
        # "rd":3
    }

    print(isChitoitsu(d))