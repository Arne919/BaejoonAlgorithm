N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visited = [False] * N
result = []

def backtrack():
    if len(result) == M:
        print(*result)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            result.append(numbers[i])
            backtrack()
            result.pop()
            visited[i] = False

backtrack()
