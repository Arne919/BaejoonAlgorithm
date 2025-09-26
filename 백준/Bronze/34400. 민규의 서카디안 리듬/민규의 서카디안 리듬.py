T = int(input())
for _ in range(T):
    t = int(input())
    pos = (t + 0.5) % 25
    if pos < 17:
        print("ONLINE")
    else:
        print("OFFLINE")
