import sys
sys.stdin = open("1244.txt")


# def comb(n,r=2):  # cur, lst 배열 글로벌에서 사용할거임
#     if r == 0:
#         cur_lst = num[:]
#         a, b =cur
#         change(a, b, cur_lst)
#         print(cur_lst)
#     elif n < r:
#         return

#     else:
#         cur[r-1] = lst[n-1]
#         comb(n-1, r-1)
#         comb(n-1, r)
def recursive(i, n, lst):  # i = fixed, n = change, lst
    if n == N:  # base case
        ans[1] = toint(lst)
        ans[0] = max(ans)
        return

    elif i == length-1:
        if flag == 1:
            ans[1] = toint(lst)
            ans[0] = max(ans)
            return
        else:
            if (N - n) %2 == 0:
                ans[1] = toint(lst)
                ans[0] = max(ans)
                return
            else:
                change(length-1, length-2, lst)
                ans[1] = toint(lst)
                ans[0] = max(ans)
                return

    max_val = max(lst[i:])
    if lst[i] == max_val:
        recursive(i+1, n, lst)  # 만약 지금이 최대면 그냥 재귀 들어감
    else:
        for j in range(i+1, length):
            if lst[j] == max_val:
                change(i, j, lst)
                recursive(i+1, n+1, lst)
                change(i, j, lst)


def toint(lst):  # 리스트 넣으면 숫자로 바꿔줄거임
    value = 0
    for i in range(length):
        value += (10**(length-1-i))*lst[i]
    return value

def change(a,b, lst):  # 그냥 위치 바꾸는거
    lst[a], lst[b] = lst[b], lst[a]
    return


T = int(input())
for tc in range(1,T+1):
    num, N = input().split()

    num = list(map(int, num))
    N = int(N)
    length = len(num)  # 자릿수
    # cur = [0]*2
    # lst = [i for i in range(length)]  # 바꿀 자리 조합
    # comb(length)
    count = [0]*10
    flag = 0
    for i in num:
        count[i] += 1
    if max(count) >= 2:
        flag = 1  # flag = 1 -> same number

    ans = [0] * 2
    recursive(0, 0, num)
    print(f'#{tc} {ans[0]}')