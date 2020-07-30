def count_positives_sum_negatives(arr):
    return [len(list(filter(lambda x: x>0, arr))),sum(list(filter(lambda y: y<0,arr)))] if(arr ) else []