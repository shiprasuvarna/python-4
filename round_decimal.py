#24) Write a Python program to round a decimal value to the nearest multiple of 0.10, unless already
#an exact multiple of 0.05. Use decimal.Decimal
from decimal import Decimal
def round_to_10_cents(x):
    remainder = x.remainder_near(Decimal('0.10'))
    if abs(remainder) == Decimal('0.05'):
        return x
    else:
        return x - remainder
# Test code.
for x in range(80, 120):
    y = Decimal(x) / Decimal('1E2')
    print("{0} rounds to {1}".format(y, round_to_10_cents(y)))
