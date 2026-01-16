import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    
    for _ in range(M):
        input()
    
    if M <= N:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
