import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

for i in range(N - 1):
    for j in range(M - 1):
        if grid[i][j] == '1' and grid[i+1][j] == '1' and grid[i][j+1] == '1' and grid[i+1][j+1] == '1':
            print(1)
            exit()

print(0)
