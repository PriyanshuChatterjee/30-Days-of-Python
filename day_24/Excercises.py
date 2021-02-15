# Importing NumPy

import numpy as np

# print('numpy: ', np.__version__)
# print(dir(np))

# Creating intnumpy array 

python_list = [1,2,3,4,5]

print('Type: ',type(python_list))

print(python_list)

two_dimensional_list = [[0,1,2],[3,4,5],[6,7,8]]

print(two_dimensional_list)

numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(numpy_array_from_list)

# Creating float numpy arrays

num_array_from_list2 = np.array(python_list, dtype=float)
print(num_array_from_list2)

# Creating a boolean a numpy array from list

numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)

# A numpy array may have one or multiple rows and columns

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

# Converting numpy array to list

np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array: ', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list)

# Creating numpy array from tuple

python_tuple = (1,2,3,4,5)
print(type(python_tuple))
print(python_tuple)

numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))
print(numpy_array_from_tuple)

# Shape of numpy array

nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ',nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ',numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7],
[8, 9, 10, 11]])
print(three_by_four_array.shape)

# Data type of numpy array

int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

