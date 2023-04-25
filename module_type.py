#22) Write a Python program to check if a given value is compiled code or not. Also check if a given
#value is a module or not. Use types.CodeType, types.ModuleType()
import types
print("Check if a given value is compiled code:")
code = compile("print('Hello')", "sample", "exec")
print(isinstance(code, types.CodeType))
print(isinstance("print(abs(-111))", types.CodeType))
print("\nCheck if a given value is a module:")
print(isinstance(types, types.ModuleType))
