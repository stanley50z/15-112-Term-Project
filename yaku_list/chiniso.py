def isChiniso(fullhand):
    type = ""
    for tile in fullhand.keys():
        if(type == ""):
            type = tile[0]
        else:
            if(tile[0] != type):
                return False
    return True


# d = {
#     "s1":2,
#     "s3":2,
#     "s4":2,
#     "s5":2,
#     "s6":3,
#     "s8":3
#     # "rd":3
# }
# print(isChiniso(d))