import sys
sys.stdin = open("4408.txt")

t = int(input())

for tc in range(1,t+1):
    n = int(input())

    lst = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        if lst[i][0] > lst[i][1]:
            lst[i][0], lst[i][1] = lst[i][1], lst[i][0]

    lst.sort(key=lambda x: x[0])
    lst.sort(key=lambda x: x[1])
    # print(lst)

    cur = lst[0]
    cnt = 1

    for i in range(1,n):
        if cur[1] <= lst[i][0]:
            cnt += 1
            cur = lst[i]
    
    print(f'#{tc} {cnt}')



# for tc in range(1,t+1):
#     n = int(input())
#     cnts = [0] * 200
#     for _ in range(n):
#         s, e = map(int, input().split())
#         if s > e:
#             s, e = e, s

#         for i in range((s-1)//2, (e-1)//2+1):
#             cnts[i] += 1
#     ans = max(cnts)

#     print(f'#{tc} {ans}')