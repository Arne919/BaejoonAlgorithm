import sys
input = sys.stdin.readline

# 0층부터 14층, 1호부터 14호 까지 DP 테이블 생성
dp = [[0] * 15 for _ in range(15)]

# 0층 초기화
for i in range(1, 15):
    dp[0][i] = i

# 나머지 층 계산
for k in range(1, 15):
    for n in range(1, 15):
        dp[k][n] = dp[k][n-1] + dp[k-1][n]

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n])
