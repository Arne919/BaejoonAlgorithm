first = int(input())
result = []
for i in range(1, first+1):
    arr = [first, i]
    while True:
        k = arr[-2] - arr[-1]
        if k >= 0:
            arr.append(k)
        else:
            break
    if len(arr) > len(result):
        result = arr
print(len(result))
print(*result)