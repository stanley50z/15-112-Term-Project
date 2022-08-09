def isIpeiko(fullhand):
    count = 0
    for type in ['s','m','p']:
        for i in range(2,9):
            if(fullhand.get(type+str(i-1),0)==2 and fullhand.get(type+str(i),0)==2 and fullhand.get(type+str(i+1),0)==2):
                count += 1
                fullhand.pop(type+str(i-1))
                fullhand.pop(type+str(i))
                fullhand.pop(type+str(i+1))
    return count == 1