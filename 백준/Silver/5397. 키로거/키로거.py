import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

for i in range(T):
    L = list(input().rstrip())
    left = deque()
    right = deque()

    for j in L:
        if j == "<":
            if left:
                a = left.pop()
                right.appendleft(a)
        elif j == ">":
            if right:
                a = right.popleft()
                left.append(a)
        elif j == "-":
            if left:
                left.pop()
        else:
            left.append(j)
    print(''.join(left + right))