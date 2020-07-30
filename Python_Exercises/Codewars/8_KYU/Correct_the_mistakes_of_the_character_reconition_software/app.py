def correct(string):
    string = string.replace("0","O")
    string = string.replace("1","I")
    string = string.replace("5","S")
    return string

# def correct(string):
#     return string.translate(str.maketrans("501", "SOI"))