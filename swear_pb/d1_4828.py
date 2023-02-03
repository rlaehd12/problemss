"""
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
"""

import sys
sys.stdin = open("input1.txt")

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

T = int(input())

for tc in range(1, T+1):
    len_lst = int(input())
    lst = list(map(int, input().split()))

    print(f'#{tc} {maxx(lst) - minn(lst)}')