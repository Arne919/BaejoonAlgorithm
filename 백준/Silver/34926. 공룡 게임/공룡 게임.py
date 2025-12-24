import sys
input = sys.stdin.readline

N, K = map(int, input().split())
s = input().strip()

# dp[i]: i번 칸에 도달 가능 여부 (0-index 사용)
dp = [False] * N
dp[0] = True  # 1번 칸

for i in range(1, N):
    if s[i] == '#':
        continue

    # 걷기
    if dp[i - 1]:
        dp[i] = True
    # 점프
    elif i - K >= 0 and dp[i - K]:
        dp[i] = True

print("YES" if dp[N - 1] else "NO")
