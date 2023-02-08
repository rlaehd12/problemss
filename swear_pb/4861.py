import sys
sys.stdin = open("4861.txt")

def palin(lst, n, m):
    for i in lst:  # 리스트 한줄씩 검사
        for j in range(n-m+1):  # 회문 길이 따라 달라짐
            #print(i[j:j+m])
            cur_lst = i[j:j+m]
            for k in range(m//2):  # 회문 길이 절반만 검사
                if cur_lst[k] != cur_lst[-1-k]:
                    break
            else:
                return cur_lst
    else:
        return 



t = int(input())
for test_case in range(1,t+1):
    n, m = map(int, input().split())  # 길이n인 글자들에서 길이m인 회문

    lst = []
    rev_lst = ['' for _ in range(n)]

    for _ in range(n):
        lst.append(input())
    
    for i in lst:
        for j in range(n):
            rev_lst[j] += i[j]

    a = palin(lst, n, m)
    b = palin(rev_lst, n, m)

    if a == None:
        print(f'#{test_case} {b}')
    else:
        print(f'#{test_case} {a}')