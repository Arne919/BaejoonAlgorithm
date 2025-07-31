def prime(x):
  if x == 1:
    return False
  for i in range(2, int(x**0.5)+1):
    if x % i == 0:
      return False
  return True

# 1 <= n <= 123,456
# 2 <= 2*n <= 246912
n_list = list(range(1,246913))
prime_list=[]
for i in n_list:
  if prime(i):
    prime_list.append(i)

while True:
  n = int(input())
  count = 0
  if n == 0:
    break
  for i in prime_list: # 만들어 둔 소수 리스트에서 숫자 꺼내서 비교
    if n < i <= 2*n:
      count += 1
  print(count)