import sys
sys.stdin = open("1221.txt")

t = int(input())

ano_numb_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

def counting(lst, n, mx):
    cnt = [0] * (mx + 1)
    cnt_lst = [0] * n

    for i in range(n):
        cnt[lst[i]] += 1

    for i in range(mx):
        cnt[i+1] += cnt[i]
    
    for i in range(n):
        cnt[lst[i]] -= 1
        cnt_lst[cnt[lst[i]]] = lst[i] 
    
    return cnt_lst



for tesse in range(1, t+1):
    a, n = input().split()
    n = int(n)
    lst = input().split()
    
    ## 전부 숫자로 변환
    for i in range(n):  # n개 리스트 전부
        for j in range(10):  # 위에 변환표
            if lst[i] == ano_numb_lst[j]:
                lst[i] = j
    
    lst = counting(lst, n, 9)

    for i in range(n):
        for j in range(10):
            if lst[i] == j:
                lst[i] = ano_numb_lst[j]
    
    print(f'#{tesse}')
    for i in lst:
        print(i, end=' ')
    print()

    pass
