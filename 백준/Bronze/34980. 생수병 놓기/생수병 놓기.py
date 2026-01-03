N = int(input().strip())
morning = input().strip()
evening = input().strip()

cnt_morning = morning.count('w')
cnt_evening = evening.count('w')

if cnt_evening < cnt_morning:
    print("Oryang")
elif cnt_evening > cnt_morning:
    print("Manners maketh man")
else:
    if morning == evening:
        print("Good")
    else:
        print("Its fine")
