def how_much_i_love_you(n):
    d = {
        0: "not at all",
        1: "I love you", 
        2: "a little", 
        3: "a lot", 
        4: "passionately", 
        5: "madly"    
        }
    n = n%6
    return d[n]
    
