import numpy as np
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(arr_2d)

print(arr_2d[1, 2])

print(arr_2d[0:2, 1:3])


# fancy slicing
indices = [0, 2]  # [2, 0]
print(arr_2d[indices, :])

# Boolean slicing
bool_mask = arr_2d > 5
print(bool_mask)
print(arr_2d[bool_mask])
