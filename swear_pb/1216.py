import sys
sys.stdin = open("1216.txt")

for test_case in range(1,11):
    t= int(input())
    countr = 5
    countc = 5
    lst = ''
    for i in range(100):  # 그냥 문자열 한줄로 받음
        lst += input()


    for i in range(100):  # 가로줄 검사
        n = countr
        cur_lst = lst[100 * i: (100 * i) + 100]
        while n <=48:
            for j in range(100-n + 1):
                b = cur_lst[j + n-1: j + n-1 - (n//2):-1]  # 지금 검사하는거 오른쪽 반
                a = cur_lst[j:j + (n//2)]  # 왼쪽 반
                if a == b:
                    if countr < n:
                        countr = n
                    break
            n += 1
    
    for i in range(100):  # 세로줄 검사
        n = countc
        cur_lst = lst[i::100]
        while n <=48:
            for j in range(100-n + 1):
                b = cur_lst[j + n-1: j + n-1 - (n//2):-1]  # 지금 검사하는거 오른쪽 반
                a = cur_lst[j:j + (n//2)]  # 왼쪽 반
                if a == b:
                    if countc < n:
                        countc = n
                    break
            n += 1
    
    print(f'#{test_case} {max(countr, countc)}')
