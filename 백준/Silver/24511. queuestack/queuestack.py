import sys
from collections import deque
input = sys.stdin.readline

dq = deque()

n = int(input())
flag = list(map(int, input().split()))

b_values = list(map(int, input().split()))
for i in range(n):
    if flag[i] == 0:
        dq.append(b_values[i])  # queue 구조만 deque에 넣기

m = int(input())
c_values = list(map(int, input().split()))

result = []
for y in c_values:
    dq.appendleft(y)
    result.append(str(dq.pop()))  # 마지막 값 pop

sys.stdout.write(' '.join(result) + '\n')
