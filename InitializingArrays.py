import numpy as np

# All 0s matrix
a = np.zeros(5)  # the parameter is shape
print(a)
# 2D array
b = np.zeros((2, 3))  # shape is 2 by 3 matrix
print(b)
# 3D array
c = np.zeros((2, 3, 4))
print(c)

# All 1s matrix
d = np.ones((4, 3))
print(d)
e = np.ones((4, 3), dtype='int32')  # specify the data type
print(e)

# Any other number
f = np.full((2, 2), 99)  # first parameter is shape, second is the number
print(f)
g = np.full((2, 2), 88, dtype='float32')
print(g)

# Any other number (full_like), when we want you use the same shape as we previous used
h = np.full_like(c, 77)  # first parameter is the previous array, second is the number
print(h)
# or
i = np.full(c.shape, 66)  # first parameter is shape, second is the number
print(i)

# Random decimal numbers
j = np.random.rand(2, 4)  # direct give it the shape, not a tuple
print(j)

k = np.random.random_sample(c.shape)
print(k)

# Random integer values
l = np.random.randint(3, 7, size=(3, 3))  # low, high, size
print(l)

# indetity matrix (square matrix)
m = np.identity(5)
print(m)

# repeat an array
arr = np.array([1, 2, 3])
r1 = np.repeat(arr, 3, axis=0)  # repeat arr 3 times
print(r1)

arr = np.array([[1, 2, 3]])
r2 = np.repeat(arr, 3, axis=0)  # repeat arr 3 times
print(r2)
r3 = np.repeat(arr, 3, axis=1)
print(r3)

# a small project
output = np.ones((5, 5))
print(output)

z = np.zeros((3, 3))
z[1, 1] = 9
print(z)

output[1:-1, 1:-1] = z
print(output)

# copy array
arr = np.array([1, 2, 3])
b = arr.copy()
b[0] = 100
print(arr)
print(b)

c = arr # be careful
c[0] = 100
print(c)
print(arr)
