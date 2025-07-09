C, R = map(int, input().split())
K = int(input())
stage = [[0] * R for _ in range(C)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

arr = []
dir = 0
arr.append([0,0])
stage[0][0] = 1
while arr:
    x, y = arr.pop()
    if stage[x][y] == K:
        print(x+1, y+1)
        exit()
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < C and 0 <= ny < R and stage[nx][ny] == 0:
        stage[nx][ny] = stage[x][y]+1
        arr.append([nx,ny])
        continue
    else:
        dir = (dir+1)%4
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < C and 0 <= ny < R and not stage[nx][ny]:
            stage[nx][ny] = stage[x][y] + 1
            arr.append([nx,ny])
            continue
print(0)