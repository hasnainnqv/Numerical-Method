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


def Jacobi_method(arr, lim=3):
    if np.size(arr) == 0 or np.size(arr) == 1:
        return "matrix error"
    result = []
    initial_values = [0] * (len(arr))
    while True:
        emp = []
        for each_var in range(len(arr)):
            c = 0
            for cal in range(len(arr)):
                if cal != each_var:
                    c -= arr[each_var][cal] * initial_values[cal]
            c += arr[each_var][-1]
            c = c / arr[each_var][each_var]
            emp.append(round(c, lim))
        initial_values = emp
        if emp in result:
            result.append(emp)
            return result
        result.append(emp)


if __name__ == '__main__':
    arr1 = np.array([[3, 0, 1, 13], [2, -3, 0, -7], [1, 3, -10, 9]])
    arr2 = np.array([])

    a = diagonal_check(arr1)
    b = diagonal_check(arr2)

    print(Jacobi_method(a, lim=3))
    print(Jacobi_method(b, lim=4))
