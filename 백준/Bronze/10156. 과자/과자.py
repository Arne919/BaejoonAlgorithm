k, n, m = map(int, input().split())

if (k * n) >= m :
  result = (k * n) - m
else :
  result = 0

print(result)