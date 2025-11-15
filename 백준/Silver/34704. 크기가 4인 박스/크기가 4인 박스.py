import sys
import math

input_data = sys.stdin.read().strip().split()
N = int(input_data[0])
arr = list(map(int, input_data[1:]))

c1 = c2 = c3 = c4 = 0
for a in arr:
    if a == 1:
        c1 += 1
    elif a == 2:
        c2 += 1
    elif a == 3:
        c3 += 1
    elif a == 4:
        c4 += 1

boxes = 0
boxes += c4           # size 4 each need one box
boxes += c3           # size 3 each need one box
c1 = max(0, c1 - c3)  # size3 box에 size1을 채움

boxes += c2 // 2
if c2 % 2 == 1:
    boxes += 1
    c1 = max(0, c1 - 2)  # 남은 size2 박스에 size1 두 개까지 넣음

if c1 > 0:
    boxes += (c1 + 3) // 4  # ceil(c1/4)

print(boxes)
