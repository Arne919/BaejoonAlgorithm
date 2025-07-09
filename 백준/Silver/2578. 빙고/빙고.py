bingo = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]
# print(bingo)
# print(mc)

#빙고 몇 줄인지 체크용
def check(play):
    cnt = 0                 # 빙고 카운트
    # 가로
    for i in play:
        if sum(i) == 0:
            cnt += 1
    # 세로
    for i in range(5):
        total = 0
        for j in play:
            if j[i] == 0:   # 불린 숫자 부분은 0임
                total += 1
        if total == 5:      # 한 열이 다 0이면 빙고 1줄
            cnt += 1

    total = 0
    j = 0
    # 우하 대각선
    for i in range(5):
        if play[i][j] == 0:
            total += 1
        j += 1
    else:
        if total == 5:
            cnt+=1

    total = 0
    j = 0
    # 우상 대각선
    for i in range(4, -1, -1):
        if play[i][j]  ==0:
            total += 1
        j += 1
    else:
        if total ==5:
            cnt +=1
    return cnt


cnt1 = 0        # 번호 인덱스
play = []
for i in mc:    # 번호 부르는거
    for j in i: # i행꺼부터
        cnt1 += 1
        for k in bingo:
            if j in k:  # 부른 번호가 빙고에 있으면
                k[k.index(j)] = 0   # 그번호 0으로 변경
                if check(bingo) >= 3:   # 만약 빙고 3줄되면
                    play.append(cnt1)   # 그번호 호출하기위해 추가
print(play[0])