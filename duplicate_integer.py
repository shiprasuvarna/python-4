#Write a Python program to find out if a given array of integers contains any duplicate elements. Return true if any value appears at least twice in
#the array, and return false if every element is distinct
def test_duplicate(array_nums):
    nums_set = set(array_nums)
    return len(array_nums) != len(nums_set)
print(test_duplicate([1,2,3,4,5]))
print(test_duplicate([1,2,3,4, 4]))
print(test_duplicate([1,1,2,2,3,3,4,4,5]))
