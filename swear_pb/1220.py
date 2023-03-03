import sys
sys.stdin = open("1220.txt")

for test_case in range(1,11):

    ##############다른 풀이 # 1다음 2 있으면 교착,0은 무시
    # [1] 전치행렬 변환, 행 단위로 처리
    # ans = 0
    # N = int(input())
    # arr = [list(map(int, input().split())) for _ in range(N)]
    # arr_t = list(zip(*arr))
    # for lst in arr_t:
    #     prev = 0
    #     for n in lst:
    #         if n != 0:
    #             if n==2 and prev == 1:
    #                 ans += 1
    #             prev = n

    ############## 또 다른거
    ans = 0
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    for st in zip(*arr):
        ans += "".join(st).replace('0', '').count('12')
    ##############

    # n = int(input())

    # ns_lst = [[] for _ in range(100)]  # column 별로 2차원 리스트 생성
    # lst = []
    # ans = 0

    # for i in range(100):  # 그냥 스트링 형태로 1차원에 받음
    #     lst += input().split()
    
    # for i in range(100):  # 각 열에 있는 1이나 2 2차원리스트에 받음
    #     for j in lst[i::100]:
    #         if j == '1' or j == '2':
    #             ns_lst[i].append(j)
    
    # for i in range(100):  # 1은 아래, 2는 위로 가니까 아래 위에 있는 1 2는 다 없앰
    #     while ns_lst[i][0] == '2':
    #         ns_lst[i].pop(0)
    #     while ns_lst[i][-1] == '1':
    #         ns_lst[i].pop(-1)
    
    # # print(ns_lst[5])

    # before = '1'
    # for i in range(100):
    #     for cur in ns_lst[i]:
    #         if cur == '2' and before == '1':  # 2 뒤에 1 있으면 뭉쳤다고 침
    #             ans += 1
    #         before = cur
    
    # #ans += 1  # 문제 잘못 이해했나..?
    
    print(f'#{test_case} {ans}')