expression = input()

parts = expression.split('-')
initial = sum(map(int, parts[0].split('+')))
result = initial
for part in parts[1:]:
    result -= sum(map(int, part.split('+')))

print(result)
