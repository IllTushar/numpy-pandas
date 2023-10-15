import numpy as np

arr = np.array([1, 2, 3, 4])
# print(arr[1])
# print(arr[1] + arr[2])

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr1[0, 1])....arr[row,index]

arr2 = np.array([1, 2, 3], ndmin=3)
# print(arr2) [[[1 2 3]]]
'''
for 3-D
[dimension,col,index]
'''
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr3[0, 1, 2])
print(arr3[0, 1, -1])
'''
[dimension, col ,lastIndexElement(-)]
'''
