from TermProject.yaku_list.toitoiho import isToi
def isSananko(handgroups,ankan=0):
    count = 0
    for group in handgroups:
        if(isToi(group) and len(group)==3):
            count += 1
    if(count + ankan == 3):
        return True
    else:
        return False