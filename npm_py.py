import numpy as np

print(np.__version__)

# array
arr_zeros = np.zeros((2, 3))

# Basic indexing
arr_1d = np.array([10, 20, 30, 40, 50])
print(type(arr_1d))
print("1D Array", arr_1d)
print("First Element at index 1", arr_1d[1])
