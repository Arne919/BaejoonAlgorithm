import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    a %= 10

    # 0이면 10번 컴퓨터
    if a == 0:
        print(10)
        continue

    # 일의 자리 패턴
    patterns = {
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1],
    }

    pattern = patterns[a]
    index = (b - 1) % len(pattern)
    result = pattern[index]

    if result == 0:
        print(10)
    else:
        print(result)
