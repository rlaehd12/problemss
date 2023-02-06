import sys
sys.stdin = open("d3_2.txt")

t = int(input())

for test_case in range(1,t+1):
    lst = list(map(int, input().split()))
    n = len(lst)
    iszero = 0
    count = 0

    for i in range(1 << n):  # 1을 왼쪽으로 n만큼, 여기 n은 10 이니까 10000000000, 1024
        subset_lst = []  # 부분집합 담을 리스트
        for j in range(n):  # 10개 껐다켰다 할거니까
            if i & (1<<j):  # 0000... 부터 1111.... 까지 각 위치 켜짐꺼짐 유무 조사
                #print(lst[j], end= ' ')
                subset_lst.append(lst[j])  # 켜있으면 부분집합 리스트에 매달음
        if sum(subset_lst) == 0:  # 하나 완성되면 다 더해봄
            count += 1
            if count ==2:  # 공집합 말고 또 0인거 있으면 
                iszero = 1
    
    print(f'#{test_case} {iszero}')