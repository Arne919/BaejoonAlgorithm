N = int(input())
dice = [list(map(int, input().split())) for _ in range(N)]
up_down = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
# print(dice)
result = []
for i in range(6):                  # 바닥이 1~6일때
    max_dice = []                   # 몸통중 큰 수 리스트(주사위당 1개)
    first = [1,2,3,4,5,6]           # 첫번째 주사위 숫자
    bottom = dice[0][i]             # 첫번째주사위 바닥
    upper = dice[0][up_down[i]]     # 첫번째주사위 천장
    first.remove(bottom)            # 바닥 제거
    first.remove(upper)             # 천장 제거
    max_dice.append(max(first))     # 몸통중에 큰수 추가
    for j in range(1, N):           # 첫번째주사위 제외(그다음)
        next = [1,2,3,4,5,6]        # 다음 주사위 숫자
        bottom = upper              # 현주사위바닥=이전주사위천장
        upper_index = up_down[dice[j].index(upper)]
        upper = dice[j][upper_index]# 현주사위 천장
        next.remove(bottom)         # 현주사위 바닥 제거
        next.remove(upper)          # 현주사위 천장 제거
        max_dice.append(max(next))  # 몸통중에 큰수 추가
    # print(result)                   # 맨바닥이 1~6일때 max총합 list
    result.append(sum(max_dice))
print(max(result))