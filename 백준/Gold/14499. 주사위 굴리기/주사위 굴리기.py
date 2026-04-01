def turn(direction, x, y):
    global dice

    # 오른
    if direction == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    # 왼
    elif direction == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    # 위
    elif direction == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    # 아래
    else:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

    # 지도의 값이 0이면 주사위 바닥에 있는 값 복사
    if data[x][y] == 0:
        data[x][y] = dice[-1]
    # 그렇지 않으면 주사위 바닥에 지도의 값 복사 후, 지도 0 초기화 
    else:
        dice[-1] = data[x][y]
        data[x][y] = 0

n, m, x, y, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
cmds = list(map(int, input().split()))
dice = [0] * 6

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for cmd in cmds:
    nx = x + dx[cmd - 1]
    ny = y + dy[cmd - 1]

    if 0 <= nx < n and 0 <= ny < m:
        turn(cmd, nx, ny)
        print(dice[0])
        x, y = nx, ny