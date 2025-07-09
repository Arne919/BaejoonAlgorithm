arr = []
rectangle = [list(map(int, input().split())) for _ in range(4)]
for k in range(4):
    x1, y1, x2, y2 = rectangle[k][0], rectangle[k][1], rectangle[k][2], rectangle[k][3]
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr.append([i, j, i+1, j+1])
result = []
for i in arr:
    if i not in result:
        result.append(i)
print(len(result))