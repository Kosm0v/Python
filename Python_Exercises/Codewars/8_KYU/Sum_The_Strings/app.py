def sum_str(a, b):
    if( a == "" and b != "" ):
        a = 0
        return  str(int(a)+int(b))
    elif( b == "" and a != "" ):
        b = 0
        return  str(int(a)+int(b))
    elif(a == "" and b == ""):
        return str(0)
    else:
        return str(int(a)+int(b))


### BEST ###

# def sum_str(a, b):
#     return str(int(a or 0) + int(b or 0))