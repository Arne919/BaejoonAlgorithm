A = int(input().strip())
B = int(input().strip())
C = int(input().strip())

result = str(A * B * C)

for i in range(10):
    print(result.count(str(i)))
