import sys
input = sys.stdin.readline

n = int(input())
wine = [0]  # 1-based index 사용
for _ in range(n):
    wine.append(int(input()))

if n == 0:
    print(0)
elif n == 1:
    print(wine[1])
elif n == 2:
    print(wine[1] + wine[2])
else:
    dp = [0] * (n + 1)
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]

    for i in range(3, n + 1):
        dp[i] = max(
            dp[i - 1],
            dp[i - 2] + wine[i],
            dp[i - 3] + wine[i - 1] + wine[i]
        )

    print(dp[n])
