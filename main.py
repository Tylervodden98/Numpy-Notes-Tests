import numpy as np
from numpy.random import default_rng

# Vectors 1d Arrays

# Matrices 2d Arrays

# Tensors 3d Arrays

# Creating Arrays
# Tuple is (Num of Arrays, Size of Array)
# 2 Arrays, of 3 Size
a1 = np.zeros(shape=(2, 3), dtype="i")
print(a1)
print(type(a1[0][0]))

# Element Operations

# Sorting
a2 = np.empty(shape=(2, 2))
print(a2)
a3 = np.sort(a2)
print(a3)

# Adding

add_arr = np.concatenate((a2, a3))
print(add_arr)

# Axes
print(add_arr.ndim)

# Shape
print(add_arr.shape)

# Size
print(add_arr.size)

# Reshaping Arrays
# Newshape is valid iff size is same as original size

# So add_arr is (4,2) so new size must have 8 elements
reshape_arr = add_arr.reshape((2, 4))
print(reshape_arr)

# Adding Axes
new_axis = reshape_arr[np.newaxis, :]
print(new_axis)

expand_axis = np.expand_dims(reshape_arr, axis=0)
print(expand_axis)

# Indexing/ Slicing
# Same as python [start:stop] or conditions arr[condition]

# Stacking/ Splitting
# np.vstack, np.hstack, np.split

# Views/Copies
# Views - Copies array but if it is changed, original is changed
b1 = reshape_arr[:]
b1[0][0] = 5
print()
print(b1)
# Original
print()
print(reshape_arr)

# Copies - Copies array but makes it a seperate object, just like in Python
b2 = reshape_arr.copy()
b2[0][0] = 100
print()
print(f"New array w using .copy {b2}")

print()
print(f"Original remains unchanged {reshape_arr}")

# Can use normal operators on Arrays
# Can use a scalar on an array, performs operation on all elements

# RNG in NumPy
rng = default_rng()
# Generate random arr of size 3x3 and integers 0-9
random_arr = rng.integers(10, size=(3, 3))
print(random_arr)

# Unique Items and Counts
a = np.array([11, 11, 12, 12, 5, 5, 4, 4, 3, 8, 9, 10, 9, 2, 1])
unique_values, indices_list, return_counts = np.unique(
    a, return_index=True, return_counts=True)
print(unique_values)
print(indices_list)
print(return_counts)

# Can Transpose Matrix

# Reverse Array with np.flip(arr)

# Can use ndarray.flatten() to turn matrix into 1d array
# ndarray.ravel() same thing but new arr KEEPS memory linked to original
