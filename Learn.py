import numpy as np

# 1D NumPy array
a = np.array([1, 2, 3])  # inside is a list
print(a.shape)  # get shape
print(a)
print(a.ndim)  # get dimension
print(a.dtype)  # get Type
print(a.itemsize)  # get size
print(a.size)  # get item numbers
print(a.size * a.itemsize)  # get total size
print(a.nbytes)  # same as total size

a = np.array([1, 2, 3], dtype='int16')  # specify the data type for the array
print(a.shape)  # get shape
print(a)
print(a.ndim)  # get dimension
print(a.dtype)  # get Type
print(a.itemsize)  # get size
print(a.size)  # get item numbers
print(a.size * a.itemsize)  # get total size
print(a.nbytes)  # same as total size

# 2D NumPy array
b = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])  # there are 2 lists in a list
print(b.shape)  # get shape
print(b)
print(b.ndim)  # get dimension
print(b.dtype)  # get type
print(b.itemsize)  # get size
print(b.size)  # get item numbers
print(b.size * b.itemsize)  # get total size
print(b.nbytes)  # same as total size
