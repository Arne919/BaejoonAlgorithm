import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

INF = 10**15
dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(cur, visited):
    # 모든 도시 방문 완료
    if visited == (1 << N) - 1:
        # 출발 도시(0)로 돌아갈 수 있으면 비용 반환
        return W[cur][0] if W[cur][0] != 0 else INF

    if dp[cur][visited] != -1:
        return dp[cur][visited]

    min_cost = INF
    for next_city in range(N):
        # 아직 방문 안 했고, 길이 있는 경우
        if not (visited & (1 << next_city)) and W[cur][next_city] != 0:
            cost = W[cur][next_city] + tsp(
                next_city,
                visited | (1 << next_city)
            )
            min_cost = min(min_cost, cost)

    dp[cur][visited] = min_cost
    return min_cost

# 시작: 도시 0, 방문 상태는 0번 도시만 방문
print(tsp(0, 1 << 0))
