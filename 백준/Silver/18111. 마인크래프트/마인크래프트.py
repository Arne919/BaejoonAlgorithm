import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
init_map = []
for i in range(n):
    init_map += list(map(int, input().split())) ## 리스트를 1차원으로 늘여 받음

ans_t, ans_h = 500*500*256*2, 0

for height in range(max(init_map), min(init_map)-1, -1): # 가능한 높이를 큰 순서대로 탐색
    block_now = sum(init_map) # 현재 나와있는 블록
    inventory = b # 인벤토리 안의 블록
    time = 0 # 초기 소요시간
    
    if block_now + b >= height*n*m: # 만들 수 있다면
        
        for block in init_map:
            if block > height: # 목표 높이보다 현재 블록이 높은 경우
                time += 2*(block-height)
                inventory += (block-height)
            else: # 목표 높이보다 현재 블록이 낮거나 같은 경우
                time += (height-block)
                inventory += (block-height) # 음수값을 더해준다 (빼주게 되는 효과)
    
        if ans_t > time: # 만들 수 있는 경우에 한해서만 업데이트
            ans_t, ans_h = time, height
        
print(ans_t, ans_h)