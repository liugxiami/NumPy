import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)
# get a specific element  [r,c]
print(a[1, 5])  # second row, sixth column number
# we also use negative index, the last one is -1
print(a[1, -1])  # second row, last number
# get a specific row
print(a[0, :])  # get first row
# get a specific column
print(a[:, 2])  # get third column
# getting a little more fancy [startindex:endindex:stepsize]
print(a[0, 1:-1:2])  # get first row from second to last number, step 2(get every other one) [2,4,6]
# change an element
a[1, 5] = 20  # change second row sixth column number to 20
print(a)
a[:, 2] = 5  # change all of the third column numbers into 5
print(a)
a[:, 2] = [30, 100]  # change the third column numbers into specific numbers, same shape
print(a)

# 3D example
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)
# get specific element (work outside in)
print(b[0, 1, 1])  # get the number 4, which is located in first layer index is 0,
# second layer index is 1, third layer index is 1
print(b[:, 1, :])  # get the arrays which's second layer's index is 1
print(b[:, 0, 0])  # get the number which's second layer's index is 0 and third layer's index is 0
# replace
b[:, 1, :] = [[9, 9], [10, 10]]
print(b)
