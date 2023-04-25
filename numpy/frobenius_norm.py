#43) Write a NumPy program to calculate the Frobenius norm and the condition number of a given
#array.
import numpy as np
a = np.arange(1, 10).reshape((3, 3))
print("Original array:")
print(a)
print("Frobenius norm and the condition number:")
print(np.linalg.norm(a, 'fro'))
print(np.linalg.cond(a, 'fro'))
