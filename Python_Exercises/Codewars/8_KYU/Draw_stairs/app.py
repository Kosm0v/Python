def draw_stairs(n):
    str = ""
    for i in range(n):
        str = str + " "*i + "I\n"
    return str[:-1]