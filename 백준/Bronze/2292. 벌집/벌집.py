N = int(input())

layer = 1     # 지나가는 방 개수(중앙 포함)
max_num = 1   # 현재 layer에서의 최대 방 번호

while max_num < N:
    max_num += 6 * layer
    layer += 1

print(layer)
