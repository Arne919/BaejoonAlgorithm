import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

count = { -1: 0, 0: 0, 1: 0 }

def check(x, y, size):
    first = paper[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first:
                return False
    return True

def divide(x, y, size):
    if check(x, y, size):
        count[paper[x][y]] += 1
        return
    
    new_size = size // 3
    for i in range(3):
        for j in range(3):
            divide(x + i * new_size, y + j * new_size, new_size)

divide(0, 0, N)

print(count[-1])
print(count[0])
print(count[1])
