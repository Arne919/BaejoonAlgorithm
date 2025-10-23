import sys
input = sys.stdin.readline

N = int(input())
matrices = [tuple(map(int, input().split())) for _ in range(N)]

# p 배열 구성
p = [matrices[0][0]] + [c for _, c in matrices]

dp = [[0] * (N + 1) for _ in range(N + 1)]

for length in range(2, N + 1):
    for i in range(1, N - length + 2):
        j = i + length - 1
        min_val = float('inf')
        pi_1 = p[i - 1]
        pj = p[j]
        dpi = dp[i]
        for k in range(i, j):
            val = dpi[k] + dp[k + 1][j] + pi_1 * p[k] * pj
            if val < min_val:
                min_val = val
        dp[i][j] = min_val

print(dp[1][N])
