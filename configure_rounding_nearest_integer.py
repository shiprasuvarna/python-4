#26) Write a Python program to configure rounding to round to the nearest integer, with ties going to
#the nearest even integer. Use decimal.ROUND_HALF_EVEN
import decimal
print("Configure the rounding to round to the nearest, with ties going to the nearest even")
decimal.getcontext().prec = 1
decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
print(decimal.Decimal(10) / decimal.Decimal(4))
