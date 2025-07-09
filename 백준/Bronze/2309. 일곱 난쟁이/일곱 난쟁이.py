arr = list(int(input()) for _ in range(9))
total = sum(arr)

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if total-arr[i]-arr[j] == 100:
            num1, num2 = arr[i], arr[j]
            break

arr.remove(num1)
arr.remove(num2)
arr.sort()

for i in arr:
    print(i)