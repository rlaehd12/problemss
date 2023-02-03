import sys
sys.stdin = open("input6485.txt")

t = int(input())

### 내 풀이
# for tc in range(t):
#     N = int(input())

#     ab_lst = []  # ab받는거 초기화

#     for i in range(N):
#         ab_lst.append(list(map(int, input().split())))

#     P = int(input())
#     c_lst = [0] * P  # c 받는거 초기화
#     bus_to_station_lst = [0] * P


#     for idx in range(P):
#         c = int(input())

#         for bus in ab_lst:
#             if (bus[0] <= c) and (c <= bus[1]):
#                 bus_to_station_lst[idx] += 1
    
#     print(f'#{tc}', end=' ')
#     for buss in bus_to_station_lst:
#         print(buss, end=' ')
#     print('')


### 교수님 풀이
for test_case in range(1, t + 1):
    N = int(input())
    # 1. N번 반복하면서 노선 입력, 빈도수 표시
    cnts = [0] * 5001
    for _ in range(N):
        S, E = map(int, input().split())
        for i in range(S, E + 1):
            cnts[i] += 1
    
    P = int(input())
    alst = []
    for _ in range(P):
        p = int(input())
        alst.append(cnts[p])

    print(f'#{test_case}', *alst)
