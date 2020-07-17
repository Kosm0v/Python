def well(x):
    if(x.count("good") in [1,2]):
        return "Publish!"
    elif(x.count("good") > 2):
        return "I smell a series!"
    else:
        return "Fail!"
        