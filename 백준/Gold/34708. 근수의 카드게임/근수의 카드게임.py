N, K = map(int, input().split())

# 최소 가능한 합은 모든 턴에서 2를 고르는 경우인 2N
if 2 * N > K:
    print(-1)
else:
    print(min(2 * N, K - 1))
