import sys
input = sys.stdin.readline

INF = float('inf')

n = int(input())   # 도시 개수
m = int(input())   # 버스 개수

# 거리 배열 초기화
dist = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용 = 0
for i in range(1, n + 1):
    dist[i][i] = 0

# 버스 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # 같은 노선 여러 개 있을 수 있으므로 최소 비용만 저장
    if c < dist[a][b]:
        dist[a][b] = c

# 플로이드-워셜 알고리즘
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == INF:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()
