N, M = map(int, input().split())
baskets = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    # 구간 [i-1:j] 역순 처리
    baskets[i-1:j] = reversed(baskets[i-1:j])

print(*baskets)
