#19) Write a Python program to construct a seeded random number generator, also generate a float
#between 0 and 1, excluding 1. Use random.random()
import random
print("Construct a seeded random number generator:")
print(random.Random().random())
print(random.Random(0).random())
print("\nGenerate a float between 0 and 1, excluding 1:")
print(random.random())
