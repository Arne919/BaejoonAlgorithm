import sys
from collections import deque
input = sys.stdin.readline

# 입력
string = list(input().strip())

deque = deque()

# 태그 출력 함수
def printTag(q):
    while q:
        print(q.popleft(), end='')

# 단어 출력 함수
def printWord(q): 
    while q:
        print(q.pop(), end='')

# '<'이 데크에 들어있는지 확인할 수 있는 변수
# 0 이면 없음, 1 이면 있음
pre = 0

for x in string:
    if x == '<':
        pre = 1 # 데크 안에 '<' 있음을 표시
        printWord(deque)
        deque.append(x)
    elif x == '>' and pre == 1: # 데크 안에 '<' 있음 -> 태그
        printTag(deque)
        print(x, end='')
        pre = 0 # 처리 후 다시 0
    elif x == ' ' and pre == 0: # 데크 안에 '<' 없음 -> 단어
        printWord(deque)
        print(x, end='')
    else: # 그 외에는 데크에 추가
        deque.append(x)

printWord(deque)