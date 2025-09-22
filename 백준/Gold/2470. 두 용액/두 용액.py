import sys

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    left, right = 0, N - 1
    best_sum = float("inf")
    ans = (arr[left], arr[right])
    
    while left < right:
        s = arr[left] + arr[right]
        
        if abs(s) < best_sum:
            best_sum = abs(s)
            ans = (arr[left], arr[right])
        
        if s == 0:
            break  # 더 이상 갱신 불가능 (최적)
        elif s < 0:
            left += 1
        else:
            right -= 1
    
    print(ans[0], ans[1])

if __name__ == "__main__":
    main()
