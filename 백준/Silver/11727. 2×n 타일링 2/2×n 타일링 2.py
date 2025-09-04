import sys

MOD = 10007
n = int(sys.stdin.readline())

dp = [0] * (n + 2)
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % MOD

print(dp[n] % MOD)
