N = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0

for k in range(N):
    target = arr[k]
    left, right = 0, N - 1
    
    while left < right:
        if left == k:  # 자기 자신 건너뛰기
            left += 1
            continue
        if right == k:  # 자기 자신 건너뛰기
            right -= 1
            continue

        s = arr[left] + arr[right]
        
        if s == target:
            count += 1
            break
        elif s < target:
            left += 1
        else:
            right -= 1

print(count)
