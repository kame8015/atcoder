from decimal import Decimal

L = Decimal(input())
v = Decimal(L / 3)
w = Decimal(v)
h = Decimal(w)

print(Decimal(v * w * h))
