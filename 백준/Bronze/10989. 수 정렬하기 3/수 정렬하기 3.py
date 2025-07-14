import sys

input = sys.stdin.readline
MAX = 10001
count = [0] * MAX

n = int(input())
for _ in range(n):
    num = int(input())
    count[num] += 1

write = sys.stdout.write
for i in range(1, MAX):
    for _ in range(count[i]):
        write(f"{i}\n")
