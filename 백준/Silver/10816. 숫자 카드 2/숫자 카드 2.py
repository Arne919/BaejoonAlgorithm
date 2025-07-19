import sys
from collections import Counter

input = sys.stdin.readline
_ = int(input())
cards = list(map(int, input().split()))
_ = int(input())
queries = list(map(int, input().split()))

card_counter = Counter(cards)

result = [str(card_counter[q]) for q in queries]
print(' '.join(result))
