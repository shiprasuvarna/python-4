'''39) Write a NumPy program to evaluate Einstein’s summation convention of two given
multidimensional arrays.
Note: In mathematics, especially in applications of linear algebra to physics, the Einstein notation or
Einstein summation convention is a notational convention that implies summation over a set of
indexed terms in a formula, thus achieving notational brevity.'''
import numpy as np
a = np.array([1,2,3])
b = np.array([0,1,0])
print("Original 1-d arrays:")
print(a)
print(b)
result = np.einsum("n,n", a, b)
print("Einstein’s summation convention of the said arrays:")
print(result)
x = np.arange(9).reshape(3, 3)
y = np.arange(3, 12).reshape(3, 3)
print("Original Higher dimension:")
print(x)
print(y)
result = np.einsum("mk,kn", x, y)
print("Einstein’s summation convention of the said arrays:")
print(result)
