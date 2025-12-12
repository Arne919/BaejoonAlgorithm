import sys
sys.setrecursionlimit(10**7)

N = int(input())
parent = list(map(int, input().split()))
del_node = int(input())

# 자식 리스트 구성
children = [[] for _ in range(N)]
root = -1
for i in range(N):
    if parent[i] == -1:
        root = i
    else:
        children[parent[i]].append(i)

# 삭제된 노드 표시 배열
deleted = [False] * N

# del_node와 그 자식들을 모두 삭제
def dfs_delete(x):
    deleted[x] = True
    for c in children[x]:
        dfs_delete(c)

dfs_delete(del_node)

# 루트 자체가 삭제되었다면 리프 = 0
if deleted[root]:
    print(0)
    exit()

# 리프 노드 개수 세기
def is_leaf(x):
    # 살아있는 자식이 없는 경우
    for c in children[x]:
        if not deleted[c]:
            return False
    return True

count = 0
for i in range(N):
    if not deleted[i] and is_leaf(i):
        count += 1

print(count)
