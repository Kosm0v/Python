def first_non_consecutive(arr):
    number = arr[0]
    for i in arr:
        if number != i:
            return number+1
        else:
            number+=1
            
    return None 