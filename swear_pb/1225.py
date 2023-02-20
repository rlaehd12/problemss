import sys
sys.stdin = open("1225.txt")

# def pw(lst):
#     cnt = 0
#     while True:
#         for i in range(1,6):  # 1부터 5까지
#             lst[cnt] -= i
#             if lst[cnt] <= 0:  # 0 이하 되면 반환
#                 lst[cnt] = 0
#                 return lst
#             cnt = (cnt+1) % 8  # 8개니까 나머지로 계속 돌림



# for tc in range(1,11):
#     t = int(input())
#     lst = list(map(int, input().split()))
#     new_lst = pw(lst)
#     print(new_lst)
#     pos = new_lst.index(0) + 1


#     # print(f'#{tc} ', end='')
#     # for i in range(8):
#     #     print(new_lst[(pos+i)%8], end=' ')
#     # print()

for tc in range(10):
    N = int(input()) # test 번호
    queue = list(map(int, input().split()))

    end = True
    while end:
        for i in range(1, 6):
            a = queue.pop(0) - i
            if a <= 0:
                queue.append(0)
                end = False
                break
            queue.append(a)

    print(queue)