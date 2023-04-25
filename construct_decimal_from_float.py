#23) Write a Python program to construct a Decimal from a float and a Decimal from a string. Also
#epresent the decimal value as a tuple. Use decimal.Decimal
import decimal
print("Construct a Decimal from a float:")
pi_val = decimal.Decimal(3.14159)
print(pi_val)
print(pi_val.as_tuple())
print("\nConstruct a Decimal from a string:")
num_str = decimal.Decimal("123.25")
print(num_str)
print(num_str.as_tuple())
