#41) Write a NumPy program to compute the sum of the diagonal element of a given array
import numpy as np
m = np.arange(6).reshape(2,3)
print("Original matrix:")
print(m)
result = np.trace(m)
print("Condition number of the said matrix:")
print(result)
