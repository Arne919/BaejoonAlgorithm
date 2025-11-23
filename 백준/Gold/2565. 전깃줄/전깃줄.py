import sys

n = int(sys.stdin.readline())
lines = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lines.append((a, b))

# A 기준으로 정렬
lines.sort()

# B값들만 가져와서 LIS 수행
B = [b for _, b in lines]

# LIS 구하기 (n ≤ 100 이므로 O(N^2) 도 충분)
dp = [1] * n

for i in range(n):
    for j in range(i):
        if B[j] < B[i]:
            dp[i] = max(dp[i], dp[j] + 1)

lis_len = max(dp)

# 제거해야 하는 전깃줄 수
print(n - lis_len)
