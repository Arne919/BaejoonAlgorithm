import sys

input = sys.stdin.readline
write = sys.stdout.write

M = int(input())
S = 0  # 비트마스크

for _ in range(M):
    cmd = input().split()

    if cmd[0] == "add":
        x = int(cmd[1]) - 1
        S |= (1 << x)
    elif cmd[0] == "remove":
        x = int(cmd[1]) - 1
        S &= ~(1 << x)
    elif cmd[0] == "check":
        x = int(cmd[1]) - 1
        write("1\n" if (S & (1 << x)) else "0\n")
    elif cmd[0] == "toggle":
        x = int(cmd[1]) - 1
        S ^= (1 << x)
    elif cmd[0] == "all":
        S = (1 << 20) - 1
    else:  # "empty"
        S = 0
