#49) Write a NumPy program to create a 5x5 matrix with row values ranging from 0 to 4
import numpy as np
x = np.zeros((5,5))
print("Original array:")
print(x)
print("Row values ranging from 0 to 4.")
x += np.arange(5)
print(x)
