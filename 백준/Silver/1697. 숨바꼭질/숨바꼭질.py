from collections import deque

def bfs(n, k):
    MAX = 100000
    visited = [0] * (MAX + 1)
    queue = deque([n])

    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x]
        
        for next_pos in (x - 1, x + 1, x * 2):
            if 0 <= next_pos <= MAX and visited[next_pos] == 0:
                visited[next_pos] = visited[x] + 1
                queue.append(next_pos)

# 입력 받기
n, k = map(int, input().split())
print(bfs(n, k))
