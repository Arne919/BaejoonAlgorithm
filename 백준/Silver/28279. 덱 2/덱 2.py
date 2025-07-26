import sys
from collections import deque

input = sys.stdin.read
commands = input().splitlines()

n = int(commands[0])
dq = deque()
output = []

for i in range(1, n + 1):
    cmd = commands[i]
    if cmd[0] == '1':
        _, x = cmd.split()
        dq.appendleft(int(x))
    elif cmd[0] == '2':
        _, x = cmd.split()
        dq.append(int(x))
    elif cmd == '3':
        output.append(str(dq.popleft()) if dq else '-1')
    elif cmd == '4':
        output.append(str(dq.pop()) if dq else '-1')
    elif cmd == '5':
        output.append(str(len(dq)))
    elif cmd == '6':
        output.append('1' if not dq else '0')
    elif cmd == '7':
        output.append(str(dq[0]) if dq else '-1')
    elif cmd == '8':
        output.append(str(dq[-1]) if dq else '-1')

# 출력
sys.stdout.write('\n'.join(output))
