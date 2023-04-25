#27) Write a Python program to create a deep copy of a given list. Use copy.copy
import copy
nums_x = [1, [2, 3, 4]]
print("Original list: ", nums_x)
nums_y = copy.deepcopy(nums_x)
print("\nDeep copy of the said list:")
print(nums_y)
print("\nChange the value of an element of the original list:")
nums_x[1][1] = 10
print(nums_x)
print("\nCopy of the second list (Deep copy):")
print(nums_y)
nums = [[1, 2, 3], [4, 5, 6]]
deep_copy = copy.deepcopy(nums)
print("\nOriginal list:")
print(nums)
print("\nDeep copy of the said list:")
print(deep_copy)
print("\nChange the value of some elements of the original list:")
nums[0][2] = 55
nums[1][1] = 77
print("\nOriginal list:")
print(nums)
print("\nSecond list (Deep copy):")
print(deep_copy)
