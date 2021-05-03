import numpy as np
a = np.arange(15).reshape(3, 5)

print(a, '\n') #Array [0 -> 14] with shape (X=3 and Y=5)

print(a.shape) #Shape of Array (X-axes and Y-axes)
print(a.ndim) #Number of Axes Dimensions of Array
print(a.size) #Array Size (index)
print(a.dtype) #Datatype and it's size in bits
print(a.itemsize) #Number of Bits/Element
print(type(a), '\n') #Type of Array -> ndarray

b = np.array([1.1, 1.2, 1.3])
print(b.dtype, '\n')

'''
for arrays that have more than 1 index, should add [] within the brackets
   np.array(1.1, 1.2, 1.3) -> Wrong
   np.array([1.1, 1.2, 1.3]) -> Right
'''
c = np.array([(1.2, 3.5), (2.3, 7.2)])
print(c, '\n')

print(np.zeros((3, 3)), '\n') #Zeroing the Matrix
print(np.ones((3, 3)), '\n') #Set the Matrix by Ones

print(np.arange(0, 10, 2), '\n') #from 0 to <10, scape 2

print(np.linspace(0, 2, 9), '\n') #9 numbers from 0 to 2

x = np.array([20, 30, 40, 50])
print(x < 35) #if <35 then true, else False