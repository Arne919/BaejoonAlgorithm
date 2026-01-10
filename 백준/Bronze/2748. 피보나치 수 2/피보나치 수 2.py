n = int(input())

# 피보나치 수 저장용 리스트
fib = [0] * (n + 1)

fib[0] = 0
if n >= 1:
    fib[1] = 1

for i in range(2, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2]

print(fib[n])
