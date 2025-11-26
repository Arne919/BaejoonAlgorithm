import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

T = int(input().strip())
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
INF = 10**9

for _ in range(T):
    R, C = map(int, input().split())
    arr = [list(map(int, input().split())) for __ in range(R)]

    dist = [[INF]*C for __ in range(R)]
    heap = []

    # 테두리(바깥에서 들어오는 시작점)를 모두 힙에 넣음
    # 테두리 칸 자체가 울타리(1)이면 그 값을 초기 cost로 넣음(부숴야 함)
    for x in range(C):
        # top row
        if dist[0][x] > arr[0][x]:
            dist[0][x] = arr[0][x]
            heapq.heappush(heap, (arr[0][x], 0, x))
        # bottom row
        if dist[R-1][x] > arr[R-1][x]:
            dist[R-1][x] = arr[R-1][x]
            heapq.heappush(heap, (arr[R-1][x], R-1, x))
    for y in range(R):
        # left col
        if dist[y][0] > arr[y][0]:
            dist[y][0] = arr[y][0]
            heapq.heappush(heap, (arr[y][0], y, 0))
        # right col
        if dist[y][C-1] > arr[y][C-1]:
            dist[y][C-1] = arr[y][C-1]
            heapq.heappush(heap, (arr[y][C-1], y, C-1))

    # Dijkstra: 이동하여 칸이 1이면 +1, 0이면 +0
    while heap:
        cost, y, x = heapq.heappop(heap)
        if cost > dist[y][x]:
            continue
        for dy, dx in dirs:
            ny, nx = y+dy, x+dx
            if 0 <= ny < R and 0 <= nx < C:
                ncost = cost + (1 if arr[ny][nx] == 1 else 0)
                if ncost < dist[ny][nx]:
                    dist[ny][nx] = ncost
                    heapq.heappush(heap, (ncost, ny, nx))

    # 0칸(꽃)들만 dist 값으로 집계
    counter = defaultdict(int)
    for y in range(R):
        for x in range(C):
            if arr[y][x] == 0:
                counter[dist[y][x]] += 1

    # 키들 정렬해서 가장 큰(=가장 많이 부숴야 하는 경우)와 그 개수 출력
    # (문제 보장: 꽃(0)은 적어도 하나 존재)
    items = sorted(counter.items())
    max_breaks, count_flowers = items[-1]
    print(max_breaks, count_flowers)
