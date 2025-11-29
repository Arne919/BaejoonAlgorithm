import sys

C, N = map(int, sys.stdin.readline().split())
cities = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# dp[i] = i명의 고객을 모으기 위한 최소 비용
# C + 100 정도 범위까지 계산해도 충분
MAX_CUSTOMER = C + 100
INF = 10**9
dp = [INF] * (MAX_CUSTOMER + 1)
dp[0] = 0

for cost, customer in cities:
    for i in range(customer, MAX_CUSTOMER + 1):
        dp[i] = min(dp[i], dp[i - customer] + cost)

print(min(dp[C:]))  # C 이상 중 최소 비용 출력
