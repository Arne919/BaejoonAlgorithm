import sys
sys.setrecursionlimit(10**6)

def hanoi(n, start, mid, end, moves):
    if n == 1:
        moves.append((start, end))
    else:
        hanoi(n-1, start, end, mid, moves)
        moves.append((start, end))
        hanoi(n-1, mid, start, end, moves)

N = int(sys.stdin.readline())
total_moves = (1 << N) - 1  # 2^N - 1
print(total_moves)

if N <= 20:
    moves = []
    hanoi(N, 1, 2, 3, moves)
    for move in moves:
        print(*move)
