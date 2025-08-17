import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)

for w, v in items:
    # 뒤에서부터 갱신 (중복 방지)
    for cur_w in range(K, w - 1, -1):
        dp[cur_w] = max(dp[cur_w], dp[cur_w - w] + v)

print(dp[K])
