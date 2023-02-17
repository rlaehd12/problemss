import sys
sys.stdin = open("1859.txt")

t = int(input())

# def find_max(lst):
#     pos = lst.index(max(lst))
#     local_max = (pos * max(lst)) - sum(lst[:pos])
#     return (lst[pos+1:], local_max)

# for tc in range(1,t+1):
#     n = int(input())
#     lst = list(map(int, input().split()))
#     cnt = 0
#     while lst:  # 지역해를 구하고 그 합을 전부 답에 더함
#         lst, add = find_max(lst)
#         cnt += add
#     print(f'#{tc} {cnt}')

################ 다른 풀이

# for tc in range(1,t+1):
#     n = int(input())
#     lst = list(map(int, input().split()))

#     ans = 0
#     i = 0
#     while i<n:
#         # [1] i부터 끝까지 최대값의 index 찾기
#         i_mx = i
#         for j in range(i+1, n):
#             if lst[i_mx] < lst[j]:
#                 i_mx = j
        
#         # [2] i~i_mx까지의 최대값과의 차이 누적
#         for j in range(i, i_mx):
#             ans += lst[i_mx] - lst[j]
        
#         i = i_mx + 1
    
#     print(f'#{tc} {ans}')

################## 뒤쪽부터 접근

for tc in range(1,t+1):
    n = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    mx = 0
    for n in lst[::-1]:
        if mx > n: ans += mx - n
        else: mx = n

    print(f'#{tc} {ans}')