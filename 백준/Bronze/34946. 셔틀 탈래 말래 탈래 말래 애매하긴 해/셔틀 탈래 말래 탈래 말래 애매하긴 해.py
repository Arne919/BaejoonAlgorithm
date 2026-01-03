A, B, C, D = map(int, input().split())

shuttle_time = A + B
walk_time = C

can_shuttle = shuttle_time <= D
can_walk = walk_time <= D

if can_shuttle and can_walk:
    print("~.~")
elif not can_shuttle and not can_walk:
    print("T.T")
elif can_shuttle:
    print("Shuttle")
else:
    print("Walk")
