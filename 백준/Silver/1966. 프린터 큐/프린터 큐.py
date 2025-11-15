from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    queue = deque([(arr[i], i) for i in range(N)])
    count = 0

    while queue:
        current = queue.popleft()
        # 뒤에 더 큰 중요도가 하나라도 있으면 뒤로 보냄
        if any(current[0] < q[0] for q in queue):
            queue.append(current)
        else:
            # 인쇄
            count += 1
            if current[1] == M:      # 찾던 문서라면 출력하고 종료
                print(count)
                break
