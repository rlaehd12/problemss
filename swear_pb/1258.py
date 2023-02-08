import sys
sys.stdin = open("1258.txt")

t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))

    ans_lst = []
    cnt = 0  # 사각형 개수 셀거
    for i in range(n):
        for j in range(n):
            row_len = 0
            col_len = 0
            # 지금 조사가 0이 아니고 좌측 상단쪽이 둘다 0이거나 좌표 밖이면
            if lst[i][j] != 0 and (lst[i-1][j] == 0 or i-1 == -1) and (lst[i][j-1] == 0 or j-1 == -1):
                cnt += 1
                ni = i  # 현위치
                nj = j
                while (nj+1 < n) and (lst[i][nj+1] != 0): # 현위치가 0이 아니면 계속
                    nj += 1
                    row_len += 1
                while (ni+1 < n) and (lst[ni+1][j] != 0): # 현위치가 0이 아니면 계속
                    ni += 1
                    col_len += 1
                ans_lst.append([col_len+1, row_len+1])
    
    ans_lst.sort()
    ans_lst.sort(key= lambda x: x[0] * x[1])
    print(f'#{test_case}', end=' ')
    print(cnt,end=' ')
    for i in ans_lst:
        for j in i:
            print(j, end=' ')
    print()

