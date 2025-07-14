def digit_sum(n):
    return sum(int(d) for d in str(n))
N = int(input())
result = 0

start = max(1, N-9*len(str(N)))

for i in range(start, N):
    if i + digit_sum(i)==N:
        result = i
        break
        
print(result)