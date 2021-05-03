from scipy.special import cbrt, exp10, comb, perm, logsumexp
from scipy import linalg, integrate, special
import numpy as np

print('Cube Root is: ', cbrt(125))
print('Exponential is: ', exp10([1,10]))
print('combination is: ', comb(5, 2, exact = False, repetition=True))
print('Permutation is: ', perm(5, 2, exact = True))

#Square Matrix
matA = np.array([[4, 5], [3, 2]])
matB = np.array([[4, 7], [2, 6]])

#Determinant  function det()
print('\nDet of Mat(A) = ', linalg.det(matA), '\n')

#Inverse function inv()
print('Inv of Mat(B):\n', linalg.inv(matB), '\n')

f = lambda x : x**2 #f(x) function
#single integration with a=0 & b=1
result = integrate.quad(f, 0 , 1)
print(result)