a_len, b_len = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

sym_diff = a_set ^ b_set 

print(len(sym_diff))
