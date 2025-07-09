board = [input() for _ in range(5)]
max_len = max(len(row) for row in board)
result = ''

for col in range(max_len):
    for row in range(5):
        if col < len(board[row]):
            result += board[row][col]

print(result)
