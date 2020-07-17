import math
def calculate_tip(amount, rating):
    d = {
        "terrible": 0, #0
        "poor" : amount*5/100,
        "good" : amount*10/100,
        "great" : amount*15/100,
        "excellent" : amount*20/100
    }
    return math.ceil(d[rating.lower()]) if(rating.lower() in  d) else 'Rating not recognised'
