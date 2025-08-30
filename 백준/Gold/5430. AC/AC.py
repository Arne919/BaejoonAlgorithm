import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    p = input().strip()
    n = int(input().strip())
    arr = input().strip()[1:-1]  # 대괄호 제거
    if arr:
        dq = deque(map(int, arr.split(',')))
    else:
        dq = deque()
    
    rev = False
    error = False
    
    for cmd in p:
        if cmd == 'R':
            rev = not rev
        elif cmd == 'D':
            if not dq:
                print("error")
                error = True
                break
            if not rev:
                dq.popleft()
            else:
                dq.pop()
    
    if not error:
        if rev:
            dq.reverse()
        print("[" + ",".join(map(str, dq)) + "]")
