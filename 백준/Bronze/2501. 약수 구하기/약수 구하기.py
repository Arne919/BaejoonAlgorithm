import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())

    cnt = 0
    for d in range(1, N + 1):
        if N % d == 0:
            cnt += 1
            if cnt == K:
                print(d)
                return
    print(0)

if __name__ == "__main__":
    main()
