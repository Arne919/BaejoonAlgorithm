import sys

input = sys.stdin.readline  # 빠른 입력
N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()  # 오름차순 정렬
print(A[K-1])  # K번째(1-indexed) 값 출력
