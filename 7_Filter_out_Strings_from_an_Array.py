def filter_list(txt):
    str_list=[]
    int_list=[]
    for i in txt:
        if type(i) == str :
            str_list.append(i)
        else:
            int_list.append(i)
    return int_list

print (filter_list([1, 2, "aasf", "1", "123", 123]))