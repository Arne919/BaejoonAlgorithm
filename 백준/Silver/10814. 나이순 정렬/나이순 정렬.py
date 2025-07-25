import sys

n = int(sys.stdin.readline())
members = []

for _ in range(n):
    age, name = sys.stdin.readline().split()
    members.append((int(age), name))

members.sort(key=lambda x: x[0])

for age, name in members:
    print(age, name)
