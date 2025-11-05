import sys

N = int(sys.stdin.readline().strip())

if N == 1:
    print(1)
    sys.exit(0)
# f1 = 1, f2 = 1
f1, f2 = 1, 1
for _ in range(3, N+1):
    f1, f2 = f2, f1 + f2
print(f2)
