import sys
input = sys.stdin.readline

MOD = 15746

N = int(input().strip())
if N == 1:
    print(1)
    sys.exit(0)
if N == 2:
    print(2)
    sys.exit(0)

a, b = 1, 2  # a = f(1), b = f(2)
for _ in range(3, N+1):
    a, b = b, (a + b) % MOD

print(b)
