A, B = input().split()

revA = int(A[::-1])
revB = int(B[::-1])

print(max(revA, revB))
