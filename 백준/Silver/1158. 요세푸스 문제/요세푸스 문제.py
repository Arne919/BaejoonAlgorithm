from collections import deque

N, K = map(int, input().split())

people = deque(range(1, N + 1))
result = []

while people:
    people.rotate(-(K - 1))  # 왼쪽으로 (K-1)번 회전
    result.append(people.popleft())  # 맨 앞 요소 제거

print("<" + ", ".join(map(str, result)) + ">")
