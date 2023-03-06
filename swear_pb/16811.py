import sys

sys.stdin = open("16811.txt")

t = int(input())

for tc in range(1, t + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    exceed = N // 2
    minV = 1000
    ##################
    # lst.sort()
    #
    # for i in range(N - 2):
    #     for j in range(i + 1, N - 1):
    #         if lst[i] != lst[i + 1] and lst[j] != lst[j + 1]:
    #             A = i + 1
    #             B = j - i
    #             C = N - 1 - j
    #             if A <= exceed and B <= exceed and C <= exceed:
    #                 diff = max(A, B, C) - min(A, B, C)
    #                 if minV > diff:
    #                     minV = diff
    #
    # if minV == 1000:
    #     minV = -1
    # print(f'#{tc} {minV}')

    ########### [2] count 배열 만들기
    def f(i, j, N):
        # 누적 안한 경우 A 소, B 중, C 대
        # A = sum(cnt[1:i + 1])
        # B = sum(cnt[i + 1:j + 1])
        # C = sum(cnt[j + 1:31])
        # 누적한 경우
        A = cnt[i]
        B = cnt[j] - cnt[i]
        C = cnt[30] - cnt[j]
        if min(A, B, C) == 0:
            return -1
        elif max(A, B, C) > N // 2:
            return -1
        else:
            return max(A, B, C) - min(A, B, C)

    cnt = [0] * 31
    for x in lst:  # 크기별 개수
        cnt[x] += 1
    for i in range(1, 31):
        cnt[i] = cnt[i] + cnt[i - 1]  # 크기별 개수 누적

    for i in range(1, 29):  # 소 박스 당근 최대 크기
        for j in range(i + 1, 30):  # 중 박스 당근 최대 크기
            result = f(i, j, N)  # 포장 시도
            if result != -1 and minV > result:
                minV = result
    if minV == 1000:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {minV}')