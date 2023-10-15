import numpy as np

arr = np.array([1, 2, "tushar", 1.2])
# print(arr)
arr2 = np.array((1, 2, 3, "Tushar"))
# print(arr2.ndim) ...check the dimension of array
arr3 = np.array([[1, 2, 6], [1, 2, 3]])
# print(arr3.ndim)
arr4 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 12, 13], [19, 12, 13, 14]]], ndmin=5)  # decide the dimension
print(arr4.ndim)
'''
ndmin -> set the dimension
ndim -> get the dimension of the array
'''
