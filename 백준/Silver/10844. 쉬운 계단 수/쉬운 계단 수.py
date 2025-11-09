import sys
input = sys.stdin.readline
MOD = 1_000_000_000

N = int(input().strip())

# dp for length i: keep only previous row to save memory
prev = [0]*10
# length 1 initialization
for d in range(1, 10):
    prev[d] = 1
prev[0] = 0

for length in range(2, N+1):
    cur = [0]*10
    cur[0] = prev[1] % MOD
    cur[9] = prev[8] % MOD
    for d in range(1, 9):
        cur[d] = (prev[d-1] + prev[d+1]) % MOD
    prev = cur

print(sum(prev) % MOD)
