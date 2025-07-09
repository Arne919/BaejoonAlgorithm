N, M = map(int, input().split())
num = int(input())
cut = [list(map(int, input().split())) for _ in range(num)]
arr_r = [0, M]
arr_c = [0, N]
for k in range(num):
    x, y = cut[k][0], cut[k][1] # x: 가0/세1 , y: 좌표
    if x == 0:  #가로일때
        arr_r.append(y)
    else:       #세로일때
        arr_c.append(y)
list.sort(arr_r)
list.sort(arr_c)
# print(arr_r, arr_c)
# arr_r, arr_c 각각 리스트 요소들 사이의 거리
nr = []
nc = []
for i in range(len(arr_r)-1):
    nr.append(arr_r[i+1]-arr_r[i])
for j in range(len(arr_c)-1):
    nc.append(arr_c[j+1]-arr_c[j])
# print(nr, nc)
max_cnt = 0
for r in nr:
    for c in nc:
        cnt = r*c
        if max_cnt < cnt:
            max_cnt = cnt
print(max_cnt)