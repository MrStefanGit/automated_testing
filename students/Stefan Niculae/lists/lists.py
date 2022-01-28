def function(a ,b):
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        return(list(a_set.intersection(b_set)))
    else: return 0