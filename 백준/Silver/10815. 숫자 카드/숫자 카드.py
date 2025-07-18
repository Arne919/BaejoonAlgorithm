import sys
input = sys.stdin.readline

N = int(input())
sang_cards = set(map(int, input().split()))

M = int(input())
queries = list(map(int, input().split()))

print(' '.join(['1' if q in sang_cards else '0' for q in queries]))
