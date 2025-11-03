import sys
input = sys.stdin.readline

N = int(input())
visited = set()
count = 0

for _ in range(N):
    msg = input().strip()
    if msg == "ENTER":
        visited.clear()
    else:
        if msg not in visited:
            count += 1
            visited.add(msg)

print(count)
