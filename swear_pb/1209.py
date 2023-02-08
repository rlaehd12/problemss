import sys
sys.stdin = open('input4.txt')


for test_case in range(10):
    T = int(input())
    print(f'#{T}', end=' ')
    big_list = [] # 100 * 100 배열
    biggest1 = 0 # 가로 젤 큰거
    biggest2 = 0 # 세로 젤 큰거
    dig1 = 0 # 대각선
    dig2 = 0 # 대각선 2

    for i in range(100):
        a = list(map(int, input().split()))
        big_list.append(a)
    
    for rows in range(100):
        if biggest1 < sum(big_list[rows]):
            biggest1 = sum(big_list[rows])
    
    # 2차원 배열 1차원으로 바꾸기
    list_1_dim = sum(big_list,[])       # 2차원 배열의 경우 []+[리스트1]+[리스트2]...
    #print(list_1_dim)                  # sum은 매개변수로 받은 []에 순회가능 데이터의 모든 데이터를 더한다
    

    
    list2 = [] ##열 기준 2차원 배열 다시 만들기

    for i in range(100):########################세로열을 눕혀서 다시 2차원 배열로 만듬
        list2.append(list_1_dim[i::100])
    
    for rows in range(100):
        if biggest2 < sum(list2[rows]):
            biggest2 = sum(list2[rows])
    
    # 대각선 계산
    for i in range(100):
        dig1 += big_list[i][i]
        dig2 += big_list[i][99-i]

    compare_list = []
    compare_list.append(biggest1)
    compare_list.append(biggest2)
    compare_list.append(dig1)
    compare_list.append(dig2)

    print(max(compare_list))