import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = dict()

def insert(root, foods):
    node = root
    for food in foods:
        if food not in node.children:
            node.children[food] = Node()
        node = node.children[food]

def dfs(node, depth):
    for food in sorted(node.children):
        print("--" * depth + food)
        dfs(node.children[food], depth + 1)

N = int(input())
root = Node()

for _ in range(N):
    parts = input().split()
    k = int(parts[0])
    foods = parts[1:]
    insert(root, foods)

dfs(root, 0)
