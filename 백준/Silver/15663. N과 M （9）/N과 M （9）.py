import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
visited = [False] * N
result = []

def dfs(depth):
    if depth == M:
        print(*result)
        return

    prev = -1  # 같은 depth에서 중복 방지
    for i in range(N):
        if not visited[i] and nums[i] != prev:
            visited[i] = True
            result.append(nums[i])
            prev = nums[i]

            dfs(depth + 1)

            result.pop()
            visited[i] = False

dfs(0)
