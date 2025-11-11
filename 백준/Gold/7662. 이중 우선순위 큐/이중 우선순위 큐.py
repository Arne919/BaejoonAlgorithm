import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_h = []
    max_h = []
    visited = [False] * k  # 삽입된 원소 유효성 체크

    for idx in range(k):
        oper, num = input().split()
        num = int(num)

        if oper == 'I':
            heapq.heappush(min_h, (num, idx))
            heapq.heappush(max_h, (-num, idx))
            visited[idx] = True
        
        else:  # D 연산
            if num == 1:  # 최대 삭제
                while max_h and not visited[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    visited[max_h[0][1]] = False
                    heapq.heappop(max_h)

            else:  # 최소 삭제
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    visited[min_h[0][1]] = False
                    heapq.heappop(min_h)

    # 최종 정리
    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)
    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)

    if not min_h or not max_h:
        print("EMPTY")
    else:
        print(-max_h[0][0], min_h[0][0])
