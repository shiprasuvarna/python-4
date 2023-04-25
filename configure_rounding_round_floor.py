#25) Write a Python program to configure the rounding to round to the floor, ceiling. Use
#decimal.ROUND_FLOOR, decimal.ROUND_CEILING
import decimal
print("Configure the rounding to round to the floor:")
decimal.getcontext().prec = 4
decimal.getcontext().rounding = decimal.ROUND_FLOOR
print(decimal.Decimal(20) / decimal.Decimal(6))
print("\nConfigure the rounding to round to the ceiling:")
decimal.getcontext().prec = 4
decimal.getcontext().rounding = decimal.ROUND_CEILING
print(decimal.Decimal(20) / decimal.Decimal(6))
