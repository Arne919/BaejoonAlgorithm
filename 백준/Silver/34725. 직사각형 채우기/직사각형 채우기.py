import sys

def build_max_layout(N, M):
    K = N * M // 4
    # 행 쌍: (0, N-1), (1, N-2), ...
    row_pairs = [(i, N-1-i) for i in range(N//2)]
    # 열 쌍: (0, M-1), (1, M-2), ...
    col_pairs = [(j, M-1-j) for j in range(M//2)]

    # 초기화
    a = [[0]*M for _ in range(N)]
    id = 1
    for i, (r1, r2) in enumerate(row_pairs):
        for j, (c1, c2) in enumerate(col_pairs):
            # 현재 id를 네 꼭짓점에 배치
            a[r1][c1] = id
            a[r1][c2] = id
            a[r2][c1] = id
            a[r2][c2] = id
            id += 1

    return a

def main():
    input_data = sys.stdin.read().strip().split()
    N = int(input_data[0]); M = int(input_data[1])
    arr = build_max_layout(N, M)
    out_lines = []
    for row in arr:
        out_lines.append(" ".join(map(str, row)))
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
