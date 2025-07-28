import math

a, b = map(int, input().split())
c, d = map(int, input().split())

numerator = a * d + c * b
denominator = b * d

gcd = math.gcd(numerator, denominator)
print(numerator // gcd, denominator // gcd)
