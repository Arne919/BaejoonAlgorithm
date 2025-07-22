def check_snack_order(n, numbers):
    stack = []
    current = 1 #현재 간식받는 번호

    for num in numbers:
        while stack and stack[-1] == current:
            stack.pop()
            current += 1
        if num == current:
            current += 1
        else:
            stack.append(num)

    while stack:
        if stack[-1] == current:
            stack.pop()
            current += 1
        else:
            break

    return "Nice" if not stack else "Sad"


n = int(input())
numbers = list(map(int, input().split()))
print(check_snack_order(n, numbers))
