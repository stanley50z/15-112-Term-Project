def isSankantsu(openMelds):
    count = 0
    for group in openMelds:
        if(len(group)==4):
            count += 1
    return count == 3

# om = [('s2','s2','s2','s2'),('s5','s5','s5','s5'),('gd','gd','gd','gd')]
# print(isSankantsu(om))