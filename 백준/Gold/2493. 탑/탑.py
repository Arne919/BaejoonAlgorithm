import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

stack = []  # (index, height)
result = [0] * N

for i in range(N):
    h = heights[i]
    # 스택의 top이 현재 탑보다 작으면 수신 불가 → pop
    while stack and stack[-1][1] < h:
        stack.pop()
    # 스택에 남아있다면, 그 top이 수신 탑
    if stack:
        result[i] = stack[-1][0]
    # 현재 탑 push (인덱스는 1부터)
    stack.append((i+1, h))

print(" ".join(map(str, result)))
