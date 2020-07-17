def get_grade(*args):
    if(sum(args)//3 in range(90,101)):
        return "A"
    elif(sum(args)//3 in range(80,91)):
        return "B"
    elif(sum(args)//3 in range(70,81)):
        return "C"
    elif(sum(args)//3 in range(60,71)):
        return "D"
    else:
        return "F"
