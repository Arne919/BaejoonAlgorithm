import sys
from collections import deque

input = sys.stdin.readline
q = deque()
n = int(input())
output = []

for _ in range(n):
    cmd = input().strip()
    
    if cmd.startswith("push"):
        _, x = cmd.split()
        q.append(x)
    elif cmd == "pop":
        output.append(q.popleft() if q else "-1")
    elif cmd == "size":
        output.append(str(len(q)))
    elif cmd == "empty":
        output.append("1" if not q else "0")
    elif cmd == "front":
        output.append(q[0] if q else "-1")
    elif cmd == "back":
        output.append(q[-1] if q else "-1")

print("\n".join(output))
