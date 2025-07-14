import sys

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()

# 출력 최적화
sys.stdout.write('\n'.join(map(str, numbers)) + '\n')
