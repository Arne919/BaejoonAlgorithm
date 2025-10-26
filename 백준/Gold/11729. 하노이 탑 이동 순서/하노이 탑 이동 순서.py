def hanoi(n, start, mid, end, moves):
    if n == 1:
        moves.append((start, end))
        return
    hanoi(n - 1, start, end, mid, moves)
    moves.append((start, end))
    hanoi(n - 1, mid, start, end, moves)

n = int(input())
moves = []
hanoi(n, 1, 2, 3, moves)

print(len(moves))
for a, b in moves:
    print(a, b)
