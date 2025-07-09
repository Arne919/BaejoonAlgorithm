N = int(input())
for _ in range(N):
    team_a = list(map(int, input().split()))[1:]
    team_b = list(map(int, input().split()))[1:]
    result = 'D'
    for i in range(4, 0, -1):
        if team_a.count(i) > team_b.count(i):
            result = 'A'
            break
        elif team_a.count(i) < team_b.count(i):
            result = 'B'
            break
    print(result)