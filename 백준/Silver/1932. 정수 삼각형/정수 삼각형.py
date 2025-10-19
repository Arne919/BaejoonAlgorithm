n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

# DP 테이블 초기화
dp = [[0]*n for _ in range(n)]
dp[0][0] = triangle[0][0]

# 점화식 적용
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:  # 왼쪽 끝
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i:  # 오른쪽 끝
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

# 마지막 줄에서 최대값 출력
print(max(dp[n-1]))
