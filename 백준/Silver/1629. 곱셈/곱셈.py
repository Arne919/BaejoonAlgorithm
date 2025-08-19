import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def mod_pow(a, b, c):
    if b == 0:
        return 1
    half = mod_pow(a, b // 2, c)
    result = (half * half) % c
    if b % 2 == 1:
        result = (result * a) % c
    return result

print(mod_pow(A, B, C))
