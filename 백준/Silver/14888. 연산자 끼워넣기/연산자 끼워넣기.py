import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

max_val = -10**9
min_val = 10**9

def c_div(a, b):
    if a < 0 and b > 0:
        return -((-a) // b)
    if a > 0 and b < 0:
        return -((a) // (-b))
    if a < 0 and b < 0:
        return (-a) // (-b)
    return a // b

def dfs(idx, current, plus, minus, mul, div):
    global max_val, min_val
    if idx == N:
        max_val = max(max_val, current)
        min_val = min(min_val, current)
        return
    num = A[idx]
    if plus:
        dfs(idx+1, current+num, plus-1, minus, mul, div)
    if minus:
        dfs(idx+1, current-num, plus, minus-1, mul, div)
    if mul:
        dfs(idx+1, current*num, plus, minus, mul-1, div)
    if div:
        dfs(idx+1, c_div(current, num), plus, minus, mul, div-1)

dfs(1, A[0], plus, minus, mul, div)

print(max_val)
print(min_val)
