import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
# plus, subtraction, multiple, divide and mod
print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)
print(a % 2)
print(a ** 2)
# two arrays addition (same shape)
b = np.array([1, 0, 1, 0])
print(a + b)

# Take the sin
print(np.sin(a))
print(np.cos(a))

# For a lot more(https://docs.scipy.org/doc/numpy/reference/routines.math.html)

# Linear Algebra
a = np.ones((2, 3))
print(a)
b = np.full((3, 2), 2)
print(b)
# do the linear algebra, note the shape of array a and b, a's column = b's row and a's row = b's col
c = np.matmul(a, b)  # but not just a*b
print(c)

# Find the determinant
c = np.identity(3)
print(c)
print(np.linalg.det(c))
# more reference (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)
