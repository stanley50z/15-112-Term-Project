def isIkkitsuukan(fullhand):
    
    for type in ['p','m','s']:
        found = True
        for i in range(1,10):
            if(type+str(i) not in fullhand.keys()):
                found = False
        if(found == True): 
            return True
    return False


if __name__ == '__main__':
    d = {
        "s1":1,
        "s2":1,
        "s3":1,
        "s4":2,
        "s5":2,
        "s6":2,
        "s7":1,
        "s8":1,
        "s9":1,
        "rd":2
    }

    print(isIkkitsuukan(d))