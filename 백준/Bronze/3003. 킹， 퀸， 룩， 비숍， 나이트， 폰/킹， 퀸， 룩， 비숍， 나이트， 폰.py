found = list(map(int, input().split()))
standard = [1, 1, 2, 2, 2, 8]
result = [standard[i] - found[i] for i in range(6)]

print(*result)
