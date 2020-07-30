def multiple_of_index(arr):
    new_list = []
    for i in range(1,len(arr)):
        if(not arr[i]%i): new_list.append(arr[i])
    return new_list

# def multiple_of_index(l):
#     return [l[i] for i in range(1, len(l)) if l[i] % i == 0]