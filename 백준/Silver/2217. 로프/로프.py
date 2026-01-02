import sys

n = int(sys.stdin.readline())
ropes = [int(sys.stdin.readline()) for _ in range(n)]

ropes.sort()

max_weight = 0
for i in range(n):
    max_weight = max(max_weight, ropes[i] * (n - i))

print(max_weight)
