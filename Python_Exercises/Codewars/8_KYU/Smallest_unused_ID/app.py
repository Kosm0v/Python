def next_id(arr):
    if(arr):
        for i in range(0,len(arr)):
            if( i not in arr):
                return i
        return i+1
    else:
        return 0