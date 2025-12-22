N = input()

count = [0] * 10

for ch in N:
    count[int(ch)] += 1

# 6과 9 묶어서 계산
six_nine = count[6] + count[9]
count[6] = count[9] = (six_nine + 1) // 2

print(max(count))
