# 스도쿠 틀렸는지 검증
# 맞으면 1 틀리면 0 출력

import sys
sys.stdin = open('input1.txt')


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

    #print(sudolist)
            
    for i in range(9):
        if has_duplicates(listb[i])==True:
            print(0)
            break
        elif has_duplicates(columnlist[i])==True:
            print(0)
            break
        elif has_duplicates(sudolist[i])==True:
            print(0)
            break
    else:
        print(1)
    