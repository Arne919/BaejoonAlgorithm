import sys
sys.setrecursionlimit(10000)

def count_XY(s):
    X = 0
    Y = 0
    for i in range(len(s)-1):
        if s[i] < s[i+1]:
            X += 1
        else:
            Y += 1
    return X, Y

def feasible(current_diff, t):
    # 현재 diff = X - Y
    # 남은 쌍 수 = t
    # 최종 diff = current_diff + (2*a - t) for some integer a in [0..t]
    # 즉 가능 값은 current_diff - t, current_diff - t + 2, ..., current_diff + t (step 2)
    # 우리는 최종 diff가 -1,0,1 중 하나여야 한다.
    for target in (-1, 0, 1):
        # target must be in [current_diff - t, current_diff + t]
        if current_diff - t <= target <= current_diff + t:
            # parity check: finalDiff - current_diff == (2*a - t)  -> has same parity as t
            if ((target - current_diff) - t) % 2 == 0:
                # equivalently (target - current_diff) % 2 == t % 2
                return True
    return False

def solve():
    input = sys.stdin.readline
    N = int(input().strip())
    S = input().strip()
    used = [False]*26
    for ch in S:
        used[ord(ch)-65] = True

    # If prefix itself already stylish:
    X0, Y0 = count_XY(S)
    if abs(X0 - Y0) <= 1:
        print(len(S))
        print(S)
        return

    # Try lengths from N to 26
    letters_all = [chr(i+65) for i in range(26)]
    for m in range(N, 27):
        # need to build final length m. if m < N skip (we start from N)
        # remaining positions to fill = m - len(curr)
        found = [None]  # to capture solution
        # We'll do DFS, but with pruning via feasible()
        def dfs(curr, used_local, X, Y):
            if found[0] is not None:
                return
            k = len(curr)
            if k == m:
                if abs(X - Y) <= 1:
                    found[0] = curr
                return
            t = m - k  # remaining pairs to create including upcoming ones? careful: remaining pairs = m-1 - (k-1) = m-k
            # current_diff:
            current_diff = X - Y
            # pruning: is it possible after t future pairs to reach diff in {-1,0,1}?
            if not feasible(current_diff, t):
                return
            # try append any unused letter (order arbitrary). we can try letters in A..Z to get deterministic output
            for i in range(26):
                if not used_local[i]:
                    ch = letters_all[i]
                    used_local[i] = True
                    # new pair between curr[-1] and ch
                    if curr[-1] < ch:
                        dfs(curr + ch, used_local, X+1, Y)
                    else:
                        dfs(curr + ch, used_local, X, Y+1)
                    used_local[i] = False
                    if found[0] is not None:
                        return

        # prepare used copy and initial counts
        used_copy = used[:]
        dfs(S, used_copy, X0, Y0)
        if found[0] is not None:
            print(m)
            print(found[0])
            return

# Entry
if __name__ == "__main__":
    solve()
