import sys

input = sys.stdin.readline

n = int(input())
target = [int(input()) for _ in range(n)]

stack = []
ops = []
cur = 1 
possible = True

for x in target:
    # x까지 push
    while cur <= x:
        stack.append(cur)
        ops.append('+')
        cur += 1

    # 맨 위가 x면 pop
    if stack and stack[-1] == x:
        stack.pop()
        ops.append('-')
    else:
        possible = False
        break

if not possible:
    print("NO")
else:
    print('\n'.join(ops))
