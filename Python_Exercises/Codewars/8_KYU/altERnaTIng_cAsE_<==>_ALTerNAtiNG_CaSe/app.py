def to_alternating_case(string):
    new_txt = ""
    for i in string:
        if(i==i.upper()):
            new_txt+=i.lower()
        else:
            new_txt+=i.upper()
    return new_txt