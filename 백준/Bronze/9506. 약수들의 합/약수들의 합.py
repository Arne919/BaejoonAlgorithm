while True:
    n = int(input())
    if n == -1:
        break
    
    divisors = []
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != 1 and i != n // i:   # 짝 약수 add, but avoid adding n
                if n // i != n:
                    divisors.append(n // i)

    divisors.sort()
    s = sum(divisors)

    if s == n:
        print(f"{n} = ", end="")
        print(" + ".join(map(str, divisors)))
    else:
        print(f"{n} is NOT perfect.")
