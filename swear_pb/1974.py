# 스도쿠 틀렸는지 검증
# 맞으면 1 틀리면 0 출력

import sys
sys.stdin = open('1974.txt')

# 다른 방법
def solve(arr):
    for lst in arr:
        if len(set(lst)) != 9:
            return 0
    arr_t = list(zip(*arr))
    for lst in arr_t:
        if len(set(lst)) != 9:
            return 0
    # 격자형 체크
    for i in (0,3,6):
        for j in (0,3,6):
            lst = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(lst)) != 9:
                return 0
    
    return 1



def has_duplicates(seq):
    return len(seq) != len(set(seq))

T = int(input())
for test_case in range(1, T + 1):

    lista=[]
    listb=[]
    columnlist=[]
    sudolist=[]
    for i in range(9):# 가로
        lista=input().split()
        listb.append(lista)
        #listb는 9개씩 묶은 2차원 배열

    for i in range(9):# 세로 묶기
        lista=[]
        for j in range(9):
            lista.append(listb[j][i])
        columnlist.append(lista)
        
    sudolist = [[] for i in range(9)]
    #격자형 묶기
    for i in range(9):
        for j in range(9):
            conv_row = i//3
            conv_col = j//3
            sudolist[(3*conv_row)+(conv_col)].append(listb[i][j])

            
    for i in range(9):
        if has_duplicates(listb[i])==True:
            print(f'#{test_case} 0')
            break
        elif has_duplicates(columnlist[i])==True:
            print(f'#{test_case} 0')
            break
        elif has_duplicates(sudolist[i])==True:
            print(f'#{test_case} 0')
            break
    else:
        print(f'#{test_case} 1')
