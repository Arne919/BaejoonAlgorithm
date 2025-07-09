N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()                      # x좌표를 기준으로 정리
arr_max,max_x = 0,0             # 최대 높이, 최댓값 인덱스

for i in range(N):              # 최댓값 찾기
    if arr_max < arr[i][1]:     # 최댓값 갱신
        arr_max = arr[i][1]     
        max_x = i               # 최댓값 인덱스 저장

high_x, high_y = arr[0][0], arr[0][1]   # 첫번째기둥 변수에 저장
result = 0

# 좌->우 높은기둥만나면 면적계산
for i in range(1, max_x+1):
    if high_y < arr[i][1]:      # 원래 기둥보다 지금기둥이 높으면
        result += (arr[i][0]-high_x)*high_y     # 원래 기둥 면적 결과에 더하기
        high_x, high_y = arr[i][0], arr[i][1]   # 지금기둥을 변수에 저장

result += arr[max_x][1] 
high_x, high_y = arr[N-1][0], arr[N-1][1]   # 마지막기둥 변수에 저장

# 우->좌 높은기둥 만나면 면적계산
for i in range(N-1, max_x-1,-1):
    if high_y <= arr[i][1]:     # 원래 기둥보다 지금기둥이 높거나 같으면
        result += (high_x-arr[i][0])*high_y     # 원래 기둥 면적 결과에 더하기
        high_x, high_y = arr[i][0], arr[i][1]   # 지금기둥을 변수에 저장

print(result)