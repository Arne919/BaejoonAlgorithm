n,m = map(int,input().split())
square = [list(input()) for _ in range(n)]

side = 0

for k in range(min(n, m), 0, -1):
    for i in range(n-k):
        for j in range(m-k):
            if square[i][j] == square[i][j+k] == square[i+k][j] == square[i+k][j+k]:
               side = max(side,k+1)

if side !=0:
    print((side)**2)
else:
    print(1)