#21) Write a Python program to check if a given value is a method of a user-defined class. Use
#types.MethodType()
import types
class C:
    def x():
        return 1
    def y():
        return 1
    def b():
        return 2
print(isinstance(C().x, types.MethodType))
print(isinstance(C().y, types.MethodType))
print(isinstance(b, types.MethodType))
print(isinstance(max, types.MethodType))
print(isinstance(abs, types.MethodType))



'''True
True
False
False
False'''
