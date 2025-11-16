def egcd(a, b):
    # 반환값: (g, x, y) such that a*x + b*y = g = gcd(a,b)
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (g, x, y)

def mod_inverse(a, n):
    g, x, y = egcd(a, n)
    if g != 1:
        return None
    return x % n

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N = int(data[0]); A = int(data[1])
    # 덧셈역
    add_inv = (N - A) % N
    # 곱셈역
    mul_inv = mod_inverse(A, N)
    if mul_inv is None:
        mul_str = "-1"
    else:
        mul_str = str(mul_inv)
    print(add_inv, mul_str)

if __name__ == "__main__":
    main()
