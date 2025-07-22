def is_vps(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        else:
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

T = int(input())
for _ in range(T):
    ps = input()
    print(is_vps(ps))
