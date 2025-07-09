import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

def count_repaint(x, y):
    repaint_w = 0  # (0,0)이 W일 때
    repaint_b = 0  # (0,0)이 B일 때
    for i in range(8):
        for j in range(8):
            current = board[x+i][y+j]
            if (i + j) % 2 == 0:  # 짝수칸
                if current != 'W':
                    repaint_w += 1
                if current != 'B':
                    repaint_b += 1
            else:  # 홀수칸
                if current != 'B':
                    repaint_w += 1
                if current != 'W':
                    repaint_b += 1
    return min(repaint_w, repaint_b)

min_repaint = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        min_repaint = min(min_repaint, count_repaint(i, j))

print(min_repaint)
