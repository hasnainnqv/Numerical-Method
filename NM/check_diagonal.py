import numpy as np

def diagonal_check(arr):
    if len(arr) == 0:
        return "empty array"
    if arr.shape == (2, 1):
        return arr
    copy = []
    copy_arr = arr
    arr = arr[:, :-1]
    lst = {}
    for index, row in enumerate(arr):
        c = []
        for j in range(len(arr)):
            diag = row[j]
            if abs(diag) >= sum(abs(row)) - abs(diag):
                c.append(j)
        lst[index] = c
    dic = [i[0] for i in lst.values()]
    if len(list(dic)) != len(set(dic)):
        return []
    for equation, crt_place in lst.items():
        if len(crt_place) != 1:
            copy.append(copy_arr[equation])
        else:
            copy.append(copy_arr[crt_place[0]])
    return np.array(copy)
