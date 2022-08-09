def isToi(group):
    t = ""
    for tile in group:
        if(t == ""): t = tile
        if(tile != t): return False
    return True
def isToitoiho(groups):
    for group in groups:
        if(not isToi(group)):
            return False
    return True

if __name__ == '__main__':
    d = [('s1', 's1', 's1'), ('s5', 's5', 's5'), ('p7', 'p7', 'p7'), ('p2', 'p2')]
    print(isToitoiho(d))