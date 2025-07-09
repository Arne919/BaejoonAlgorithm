N = int(input())
arr = list(map(int, input().split()))
student = int(input())
student_arr = [list(map(int, input().split())) for _ in range(student)]


for i in range(student):
    if student_arr[i][0] == 1:          # 남학생인경우
        for j in range(1, (N // student_arr[i][1])+1):  # 숫자의 배수의 스위치
            switch = (student_arr[i][1] * j)-1
            if arr[switch] == 1:
                arr[switch] = 0
            elif arr[switch] == 0:
                arr[switch] = 1
    elif student_arr[i][0] == 2:        # 여학생인경우
        switch = student_arr[i][1]    # 3
        if N//2 >= switch:            #
            j = switch-1                # 2
            if j == 0:         # 3-2-1 =0
                if arr[0] == 1:
                    arr[0] = 0
                else:
                    arr[0] = 1
            else:
                if arr[switch-1] == 1:
                    arr[switch-1] = 0
                elif arr[switch-1] == 0:
                    arr[switch-1] = 1
                for k in range(1, j+1):
                    if arr[switch-k-1] == arr[switch+k-1]:
                        if arr[switch-k-1] == 1:
                            arr[switch - k - 1] =0
                            arr[switch + k - 1] =0
                        else:
                            arr[switch - k - 1] = 1
                            arr[switch + k - 1] = 1

                    else:
                        break
        elif N//2 < switch:
            j = N-switch                        # 8-5 = 3
            if j == 0:
                if arr[N-1] == 1:
                    arr[N-1] = 0
                else:
                    arr[N-1] = 1
            else:
                if arr[switch-1] == 1:
                    arr[switch-1] = 0
                elif arr[switch-1] == 0:
                    arr[switch-1] = 1
                for k in range(1, j + 1):
                    if arr[switch - k-1] == arr[switch + k-1]:
                        if arr[switch - k - 1] == 1:
                            arr[switch - k - 1] = 0
                            arr[switch + k - 1] = 0
                        else:
                            arr[switch - k - 1] = 1
                            arr[switch + k - 1] = 1
                    else:
                        break
        else:
            break
        # print(arr)

for l in range(1, N + 1):
    print(arr[l - 1], end= " ")
    if l % 20 == 0:
        print()