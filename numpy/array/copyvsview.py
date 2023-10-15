import numpy as np

'''
The Difference Between Copy and View
The main difference between a copy and a view of an array is that the copy is a new array, 
and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, 
and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, 
and any changes made to the original array will affect the view.
'''
arr = np.array([1, 2, 3, 4])
x = arr.copy()
arr[0] = 42
# print(arr)
# print(x)
'''
output -> [42  2  3  4]
          [1 2 3 4]
'''

arr1 = np.array([5, 6, 7, 8])
y = arr1.view()
arr1[1] = 24
# print(arr1)
# print(y)
'''
output -> [ 5 24  7  8]
          [ 5 24  7  8]
'''
print(x.base)
print(y.base)
'''
output -> None
          [ 5 24  7  8]
'''
