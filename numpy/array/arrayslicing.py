import numpy as np

'''
slicing=[starting index : last index-1]
negative slicing = [starting last index  : ending last index]
step = [starting index, last index-1, step]
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:]) print starting index to last index
# print(arr[1:3]) print starting index to last index-1
# print(arr[:3])  print the last index-1
# print(arr[-3: -1]) in negative last third to last one
# print(arr[1:4:2])

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr1[1, 0:3]) # print 2D array with slicing...
print(arr1[0:, 0:])
