#40) Write a NumPy program to compute the determinant of an array.
import numpy as np
a = np.array([[1,2],[3,4]])
print("Original array:")
print(a)
result = np.linalg.det(a)
print("Determinant of the said array:")
print(result)
