"""
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176	
"""

import sys
sys.stdin = open('input2.txt')

def maxx(lst):
    max_v = lst[0]  # 기본은 맨 앞
    for i in lst:  # 리스트 순회하면서
        if max_v < i:  # 큰값 만나면 값을 바꿈
            max_v = i
    return max_v

def minn(lst):
    min_v = lst[0]  # 기본은 맨 앞
    for i in lst:  # 리스트 순회하면서
        if min_v > i:  # 작은값 만나면 값을 바꿈
            min_v = i
    return min_v

def not_zero_minn(lst):
    min_v = lst[0]  # 기본은 맨 앞
    for i in lst:  # 리스트 순회하면서
        if (min_v > i) and (i != 0):  # 작은값 만나면 값을 바꿈
            min_v = i
    return min_v

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N은 길이, M은 이웃한거 개수
    lst = list(map(int, input().split()))
    sum_value = 0  # 묶은거 더한거 저장할 변수 생성
    ans_lst = [0] * N  # N개만큼 정답 리스트 생성

    for i in range(M):  # 첫번째 더한값 생성
        sum_value += lst[i]
    ans_lst[0] = sum_value  #0번째에 지금값 저장

    # 이제 앞에거 빼고 뒤에거 더하는 식으로 생성
    for i in range(N-M):
        sum_value += lst[i+M]
        sum_value -= lst[i]

        ans_lst[i+1] = sum_value  # 0 말고 1부터 더한 값 저장
        pass

    # 젤 큰거랑 작은거 뺌
    a = maxx(ans_lst)-not_zero_minn(ans_lst)
    print(f'#{tc} {a}')
    pass