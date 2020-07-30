def warn_the_sheep(queue):
    if(queue[-1] == "wolf"):
        return "Pls go away and stop eating my sheep"
    else:
        index_of_wolf = queue.index("wolf")
        queue.remove("wolf")    
        return "Oi! Sheep number {n}! You are about to be eaten by a wolf!".format(n = len(queue) -index_of_wolf)