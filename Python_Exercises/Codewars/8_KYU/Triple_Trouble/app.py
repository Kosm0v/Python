def triple_trouble(one,two,three):
    new = ""
    for i in range(len(one)):
        new = new + one[i] + two[i] + three[i]
    return new