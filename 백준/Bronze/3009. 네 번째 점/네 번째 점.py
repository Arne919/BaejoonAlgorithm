# 세 점의 좌표 입력
x = []
y = []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

# x, y 각각에서 하나만 등장하는 값을 찾음
for i in x:
    if x.count(i) == 1:
        ans_x = i
for i in y:
    if y.count(i) == 1:
        ans_y = i

print(ans_x, ans_y)
