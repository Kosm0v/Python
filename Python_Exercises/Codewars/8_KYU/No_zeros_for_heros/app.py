def no_boring_zeros(n):
    if(n==0 or n%10!=0):
        return n
    for i in range(100):
        if(n%10 == 0):
            n = n//10
        else:
            return n

#shortest
# def no_boring_zeros(n):
#     try:
#         return int(str(n).rstrip('0'))
#     except ValueError:
#         return 0
