#29) Write a Python program to create a deep copy of a given dictionary. Use copy.copy
import copy
nums_x = {"a":1, "b":2, 'cc':{"c":3}}
print("Original dictionary: ", nums_x)
nums_y = copy.deepcopy(nums_x)
print("\nDeep copy of the said list:")
print(nums_y)
print("\nChange the value of an element of the original dictionary:")
nums_x["cc"]["c"] = 10
print(nums_x)
print("\nSecond dictionary (Deep copy):")
print(nums_y)
nums = {"x":1, "y":2, 'zz':{"z":3}}
nums_copy = copy.deepcopy(nums)
print("\nOriginal dictionary :")
print(nums)
print("\nDeep copy of the said list:")
print(nums_copy)
print("\nChange the value of an element of the original dictionary:")
nums["zz"]["z"] = 10
print("\nFirst dictionary:")
print(nums)
print("\nSecond dictionary (Deep copy):")
print(nums_copy)
