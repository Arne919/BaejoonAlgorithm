import sys
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

INF = -10**30
dp = [[[INF]*3 for _ in range(N+1)] for __ in range(N+1)]
dp[0][0][0] = 0

for i in range(1, N+1):
    for k in range(0, i+1):
        # 1) i번에 타워 안 짓기
        dp[i][k][0] = max(dp[i-1][k])

        if k == 0:
            continue

        # 2) i번에 타워만 짓기
        dp[i][k][1] = max(
            dp[i-1][k-1][0],
            dp[i-1][k-1][1],
            dp[i-1][k-1][2]
        ) + A[i]

        # 3) i-1과 연결
        dp[i][k][2] = dp[i-1][k-1][1] + A[i] + B[i-1]

for k in range(1, N+1):
    print(max(dp[N][k]))
