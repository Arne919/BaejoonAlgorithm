import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
result = [-1] * N  # 기본값 -1로 초기화
stack = []  # 인덱스를 저장할 스택

for i in range(N):
    # 현재 값이 스택 상단 인덱스의 값보다 크다면, 오큰수 확정
    while stack and A[stack[-1]] < A[i]:
        result[stack.pop()] = A[i]
    stack.append(i)

print(*result)
