max_value = -1
row = col = 0

for i in range(9):
    nums = list(map(int, input().split()))
    for j in range(9):
        if nums[j] > max_value:
            max_value = nums[j]
            row = i + 1
            col = j + 1

print(max_value)
print(row, col)
