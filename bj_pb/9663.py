def permu(i, n):
    global cnt
    if i == n:  # base case
        cnt += 1
        # print(lst)
    else:
        for j in range(i, n):  # 현재 i-1인덱스까지 고정된 상태
            lst[i], lst[j] = lst[j], lst[i]  # 자리 바꿈
            
            if right_check[i + (n-1)-lst[i]] == 1 or left_check[i + lst[i]] == 1:
                lst[i], lst[j] = lst[j], lst[i]  # 조건에 맞지 않으면 다시 원상복귀
                continue
            else:
                right_check[i + (n - 1) - lst[i]] += 1
                left_check[i + lst[i]] += 1

            permu(i+1, n)
            # 초기화
            right_check[i + (n - 1) - lst[i]] -= 1
            left_check[i + lst[i]] -= 1
            lst[i], lst[j] = lst[j], lst[i]


n = int(input())
lst = [i for i in range(n)]
right_check = [0] * ((2*n)-1)  # 대각선 방향 체크
left_check = [0] * ((2*n)-1)
cnt = 0
permu(0, n)
print(cnt)

############## 똑같은데 더 깔끔한거
# n = int(input())
# cnt = 0
# is_used1 = [False] * n
# is_used2 = [False] * (2*n - 1)
# is_used3 = [False] * (2*n - 1)
# 
# def func(k):
#     global cnt
#     if k == n:
#         cnt += 1
#         return
#     for i in range(n):
#         if is_used1[i] or is_used2[i - k + n - 1] or is_used3[i + k]:
#             continue
#         is_used1[i] = True
#         is_used2[i - k + n - 1] = True
#         is_used3[i + k] = True
#         func(k+1)
#         is_used1[i] = False
#         is_used2[i - k + n - 1] = False
#         is_used3[i + k] = False
# 
# func(0)
# print(cnt)

####### 느린거
# def permu(i, n):
#     global cnt
#     global call
#     call += 1
#     if i == n:  # base case
#         if not check(i):
#             cnt += 1
#     else:
#         for j in range(i, n):
#             s = 0
#             lst[i], lst[j] = lst[j], lst[i]
#             if check(i):
#                 return
#             permu(i+1, n)
#             lst[i], lst[j] = lst[j], lst[i]
#
#
# def check(i):
#     global call2
#     call2 += 1
#     for j in range(i-1):
#         if abs(lst[j] - lst[i-1]) == abs(j-(i-1)):
#             return True
#     return False


# n = int(input())
# lst = [i for i in range(n)]
# cnt = 0
# call = call2 = 0
# permu(0, n)
# print(cnt)
# print(call, call2)
