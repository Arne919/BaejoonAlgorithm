N = int(input())
arr = list(map(int, input().split()))
result = []
for i in range(N):
    if arr[i] ==0:
        result.insert(0,i+1)
    else:
        result.insert(arr[i],i+1)

print(*result[::-1])
