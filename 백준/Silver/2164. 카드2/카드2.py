import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque(range(1, n + 1))

while len(q) > 1:
    q.popleft()        # 제일 위 버리기
    q.append(q.popleft())  # 다음 아래로 이동

print(q[0])
