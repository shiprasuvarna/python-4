#27) Write a Python program to create a shallow copy of a given list. Use copy.copy
import copy
nums_x = [1, [2, 3, 4]]
print("Original list: ", nums_x)
nums_y = copy.copy(nums_x)
print("\nCopy of the said list:")
print(nums_y)
print("\nChange the value of an element of the original list:")
nums_x[1][1] = 10
print(nums_x)
print("\nSecond list:")
print(nums_y)
nums = [[1], [2]]
nums_copy = copy.copy(nums)
print("\nOriginal list:")
print(nums)
print("\nCopy of the said list:")
print(nums_copy)
print("\nChange the value of an element of the original list:")
nums[0][0] = 0
print("\nFirst list:")
print(nums)
print("\nSecond list:")
print(nums_copy)
