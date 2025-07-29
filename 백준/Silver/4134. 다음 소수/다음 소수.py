import sys
import math

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def next_prime(n):
    while True:
        if is_prime(n):
            return n
        n += 1

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(next_prime(n))
