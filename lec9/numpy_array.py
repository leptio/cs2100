import numpy as np
#numpy array = nparray = n-dimensional array
#array shape defines how many elements in an array are read (6 elements arranged as a 2x3 matrix)
#array stride defines number of elements to skip in 1d layout to reach next element (how many bytes do you need to jump)
v1 = np.array([
    [1,2,3],
    [1,2,3]
])

print(np.mean(v1))

a = np.arange(6)
print("Shape:", a.shape)
print("Strides:", a.strides)

#Change into a 2-d matrix by reshaping
shape_mode: tuple[int, int] = (2,3)
a.shape = shape_mode
print(a)
print("Shape:", a.shape)
print("Strides:", a.strides)

#Transpose the array
print(a.transpose())

#Numpy broadcasting allows arrays of different shapes to work with universal function
#It automatically expands the same array
#Example: 1D vector added to each row of 2D array

s1 = np.array([
    [1,2,3],
    [4,5,6]
])
s2 = np.array([7,8,9])
#1d vector added to each row of 2d array
print(s1+s2)
