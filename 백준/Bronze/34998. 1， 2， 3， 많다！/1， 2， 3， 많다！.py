import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    X = int(input())
    expr = input().split()

    total = 0
    many = False  # '!'가 등장했는지 여부

    for i in range(0, len(expr), 2):
        val = expr[i]
        if val == '!':
            many = True
            break
        total += int(val)
        if total >= 10:
            many = True
            break

    if many:
        print('!')
    else:
        print(total)
