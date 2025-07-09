N = int(input())
arr = list(map(int, input().split()))

cnt = 1
increase = 1
decrease = 1

for i in range(N-1):
    if arr[i+1] >= arr[i]:
        increase += 1
        if increase > cnt:
            cnt = increase
        else:
            cnt
    else:
        increase = 1
for i in range(N-1):
    if arr[i+1] <= arr[i]:
        decrease += 1
        if decrease > cnt:
            cnt = decrease
        else:
            cnt
    else:
        decrease = 1
print(cnt)