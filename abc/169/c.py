import math
from decimal import Decimal

A, B = input().split()
A = Decimal(A)
B = Decimal(B)

result = math.floor(A * B)

print(result)
