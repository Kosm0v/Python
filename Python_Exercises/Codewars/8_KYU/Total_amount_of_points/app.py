def points(games):
    point = 0
    for score in games:
        score = score.split(":")
        if( int(score[0]) - int(score[1]) > 0 ):
            point += 3
        elif( int(score[0]) - int(score[1]) == 0 ):
            point += 1
    return point