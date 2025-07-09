N, K = map(int,input().split())
student = [[0,0] for _ in range(6)] # [여,남] * 6
room = 0

for i in range(N):
    S, Y = map(int,input().split())
    if S == 0:
        student[Y-1][0] += 1
    else:
        student[Y-1][1] += 1
# print(student)
for i in range(6):  # 학년
    for j in range(2):  # 성별
        room += student[i][j]//K
        if student[i][j]%K != 0:    # 남은인원있으면 room +1
            room += 1
print(int(room))