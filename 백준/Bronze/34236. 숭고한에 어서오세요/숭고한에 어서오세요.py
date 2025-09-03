N = int(input().strip())
A = list(map(int, input().split()))
d = A[1] - A[0]          # 등차수열의 공차 (양수)
print(A[-1] + d)         # 다음 대회 연도
