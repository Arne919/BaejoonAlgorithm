import sys
input = sys.stdin.readline

N = int(input())
stack = []
output = []

for _ in range(N):
    command = input().strip()

    if command.startswith("1"):
        _, num = command.split()
        stack.append(int(num))
    elif command == "2":
        if stack:
            output.append(str(stack.pop()))
        else:
            output.append("-1")
    elif command == "3":
        output.append(str(len(stack)))
    elif command == "4":
        output.append("1" if not stack else "0")
    elif command == "5":
        if stack:
            output.append(str(stack[-1]))
        else:
            output.append("-1")

# 한 번에 출력
sys.stdout.write("\n".join(output) + "\n")
