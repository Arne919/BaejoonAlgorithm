from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

# 집, 치킨집 위치 저장
for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))

# 치킨 거리 계산 함수
def city_chicken_distance(selected):
    total = 0
    for hr, hc in houses:
        dist = min(abs(hr - cr) + abs(hc - cc) for cr, cc in selected)
        total += dist
    return total

# 치킨집 조합 선택 후 최소값 찾기
answer = float("inf")
for comb in combinations(chickens, M):
    answer = min(answer, city_chicken_distance(comb))

print(answer)
