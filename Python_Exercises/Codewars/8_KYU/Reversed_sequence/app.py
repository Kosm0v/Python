def reverse_seq(n):
    seq = [] 
    for i in range(n,0,-1):
        seq.append(i)
    return seq

print(reverse_seq(5))