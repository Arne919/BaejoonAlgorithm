t = int(input())  # 테스트 케이스 개수 입력
for _ in range(t):
    quiz = input().strip()
    score = 0   # 총 점수
    cnt = 0     # 연속된 O의 개수

    for ch in quiz:
        if ch == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)
