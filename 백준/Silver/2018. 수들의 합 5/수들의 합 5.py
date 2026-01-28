import sys
input = sys.stdin.readline
N = int(input())
start = 1
end = 1
total = 1
count = 1  ## 자기 자신 포함

## 1, 2만 예외처리
if N == 1 or N == 2:
  print(1)
  sys.exit()

## 반복하며 카운트, end가 굳이 N까지 갈필요 없다고 생각해서 반복조건을 저런식으로 함.
while end < N//2 + 2:
  if total == N:
    count += 1
    end += 1
    total = total + end
  elif total < N:
    end += 1
    total = total + end
  else:
    total = total - start
    start += 1
print(count)