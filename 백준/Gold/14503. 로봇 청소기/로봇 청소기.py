N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

count = 0

while True:
    # 1. 현재 칸이 청소되지 않은 경우, 청소한다.
    if room[r][c] == 0:
        room[r][c] = 2  # 청소 완료 표시
        count += 1

    # 2. 주변 4칸 중 청소되지 않은 빈 칸이 있는지 확인
    cleaned = True
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if room[nr][nc] == 0:
            cleaned = False
            break

    if cleaned:  # 주변에 청소할 칸 없음
        # 후진
        back = (d + 2) % 4
        nr, nc = r + dr[back], c + dc[back]
        if room[nr][nc] == 1:  # 벽이면 멈춤
            break
        else:  # 벽이 아니면 후진
            r, c = nr, nc
    else:
        # 반시계 방향 회전
        d = (d + 3) % 4
        nr, nc = r + dr[d], c + dc[d]
        if room[nr][nc] == 0:  # 앞 칸이 청소되지 않았다면 전진
            r, c = nr, nc

print(count)
