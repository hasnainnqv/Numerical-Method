import numpy as np
from check_diagonal import  diagonal_check

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
    arr2 = np.array([[-3, 9, 1, 2], [5, -2, 3, -1], [2, -1, -7, -1]])

    a = diagonal_check(arr1)
    b = diagonal_check(arr2)

    # print(Jacobi_method(a, lim=3))
    print(Jacobi_method(b, lim=4))
