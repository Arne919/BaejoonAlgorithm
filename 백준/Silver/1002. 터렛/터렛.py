import math

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.dist((x1, y1), (x2, y2))  # 두 점 사이 거리

    if d == 0 and r1 == r2:
        print(-1)  # 무한대
    elif d == 0 and r1 != r2:
        print(0)   # 교점 없음
    elif d > r1 + r2:
        print(0)   # 두 원이 멀리 떨어짐
    elif d < abs(r1 - r2):
        print(0)   # 한 원이 다른 원 안에 있지만 만나지 않음
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)   # 외접 또는 내접
    else:
        print(2)   # 두 점에서 만남
