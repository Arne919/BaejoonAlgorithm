N = int(input())
arr = [[0]*1001 for _ in range(1001)]

for i in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for j in range(y, y+h):
        arr[j][x:x+w] = [i]*w
    # for j in range(x, x+w):
    #     for k in range(y, y+h):
    #         arr[j][k] = i

for i in range(1, N+1):
    result = 0
    for paper in arr:
        result += paper.count(i)
    print(result)