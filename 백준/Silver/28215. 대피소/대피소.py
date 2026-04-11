import sys
import math
from itertools import combinations
input = sys.stdin.readline

N,K = map(int,input().split())
house = []
INF = math.inf
for i in range(N):
    x,y = map(int,input().split())
    house.append([x,y])

def cal_dist(cur_house, shelter):
    return abs(house[cur_house][0]-house[shelter][0]) + abs(house[cur_house][1]-house[shelter][1])



max_dist = INF

for shelters in list(combinations(range(N),K)): # 대피소 K개를 선택
    cur_dist = -1

 # 집 별 대피소와의 거리를 계산한다.
    for cur_house in range(N):
        cur_house_dist = INF
        for shelter in shelters:
            cur_house_dist = min(cur_house_dist, cal_dist(cur_house, shelter))
        cur_dist = max(cur_dist, cur_house_dist)
    max_dist = min(max_dist, cur_dist)
print(max_dist)