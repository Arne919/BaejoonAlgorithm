import sys
input = sys.stdin.readline

T = int(input())
queries = [int(input()) for _ in range(T)]
max_n = max(queries)
#DP배열?
P = [0] * (max_n + 1)
base = [0, 1, 1, 1, 2, 2]
for i in range(1, min(max_n, 5) + 1):
    P[i] = base[i]

for i in range(6, max_n + 1):
    P[i] = P[i - 1] + P[i - 5]

print("\n".join(str(P[n]) for n in queries))
