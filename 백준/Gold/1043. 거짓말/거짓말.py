import sys
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]
true = list(map(int, input().split()))  # 진실을 아는 사람 수, 번호
partys = [list(map(int, input().split())) for _ in range(m)]

def union(a, b):
    x = find(a)
    y = find(b)
    parent[y] = x

def find(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]

if true[0] == 0:                # 진실을 아는 사람이 없으면 모든 파티에서 거짓말 가능
    print(m)
    exit()

for i in range(2, len(true)):   # 진실을 아는 사람 union
    union(true[1], true[i])

for party in partys:            # 파티마다 사람들 union
    for i in range(2, len(party)):
        union(party[1], party[i])

answer = 0
x = find(true[1])

for party in partys:
    if find(party[1]) != x:
        answer += 1

print(answer)