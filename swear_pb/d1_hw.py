import sys
sys.stdin = open("input3.txt")

def big(a,b):  # 두개 중 큰거 리턴
    if a > b:
        return a
    else:
        return b

def small(a,b):  # 두개중 작은거 리턴
    if a> b:
        return b
    else:
        return a

for tc in range(1,11):        
    N = int(input())
    sun_lst = [0] * N  # 볕드는 리스트 N개만큼 생성


    lst = list(map(int, input().split()))
    for idx in range(2, N - 2):  # 양 끝 2개씩은 볼 필요 없음
        tall_rt = big(lst[idx+1], lst[idx+2])  # 오른쪽 2개 중 큰거
        tall_lt = big(lst[idx-1], lst[idx-2])  # 왼쪽 2개 중 큰거
        if lst[idx] > tall_rt:        # 오른쪽 2개보다 더큼
            sun_lst[idx] = (lst[idx] - tall_rt)  # 뺀 값 저장
            if lst[idx] > tall_lt:       # 왼쪽 2개 보다도 더 큼
                sun_lst[idx] = small(sun_lst[idx], lst[idx] - tall_lt)  ## 둘중 작은거 저장
            else:                        # 왼쪽 2개보다 작음
                sun_lst[idx] = 0         # 0 저장
        
        pass

    summ = 0  # 출력할 값
    for i in sun_lst:
        summ += i
    print(f'#{tc} {summ}')
    pass