import sys
sys.stdin = open("1215.txt")

for test_case in range(1, 11):
    n = int(input())

    count = 0
    lst = ''
    for i in range(8):  # 그냥 문자열 한줄로 받음
        lst += input()
    # print(lst[0::8])  # 슬라이싱 하면 세로줄
    # print(lst[0:7])  # 그냥 하면 가로줄

    for i in range(8):  # 가로줄 검사
        cur_lst = lst[8 * i: (8 * i) + 8]
        for j in range(8-n + 1):
            b = cur_lst[j + n-1: j + n-1 - (n//2):-1]  # 지금 검사하는거 오른쪽 반
            a = cur_lst[j:j + (n//2)]  # 왼쪽 반
            if a == b:
                #print(a)
                count += 1
                pass
    
    for i in range(8):  # 세로줄 검사
        cur_lst = lst[i::8]
        for j in range(8-n + 1):
            b = cur_lst[j + n-1: j + n-1 - (n//2):-1]
            a = cur_lst[j:j + (n//2)]
            if a == b:
                #print(a)
                count += 1
                pass
    
    print(f'#{test_case} {count}')
