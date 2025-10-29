N, M = map(int, input().split())
lessons = list(map(int, input().split()))

left = max(lessons)        # 블루레이 최소 크기
right = sum(lessons)       # 블루레이 최대 크기
answer = right

while left <= right:
    mid = (left + right) // 2  # 블루레이 용량 후보
    count = 1                  # 사용 블루레이 개수
    total = 0                  # 현재 블루레이에 저장된 강의 길이 합
    
    for length in lessons:
        if total + length > mid:
            count += 1
            total = 0
        total += length
    
    if count <= M:   # M개 이하로 가능 → 용량 줄여보기
        answer = mid
        right = mid - 1
    else:            # M개 초과 → 용량 늘려야 함
        left = mid + 1

print(answer)
