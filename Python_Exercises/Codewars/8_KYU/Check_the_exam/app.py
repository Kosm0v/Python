def check_exam(a,b):
    score = 0
    for i in range(len(b)):
        if(b[i] == ""):
            continue
        elif(b[i] in a[i]):   
            score+=4
        else:
            score-=1
    return score if(score>0) else 0