def function(a ,b):
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        return(a_set.intersection(b_set))
    else: return 0

if __name__ == '__main__':
    print(list(function([1, 2, 3], [1, 2, 3])))