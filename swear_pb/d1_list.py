"""
3
9
7 4 2 0 0 6 0 7 0
9
7 4 2 0 0 6 7 7 0
20
52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53
"""
# 맨 앞 리스트 요소부터 뒤에 리스트에 자기 미만인 값이 있으면 +1
# 그 값들을 다른 리스트에 저장

T = int(input())

def maxx(lst):
    max_v = lst[0]  # 기본은 맨 앞
    for i in lst:  # 리스트 순회하면서
        if max_v < i:  # 큰값 만나면 값을 바꿈
            max_v = i
    return max_v

def minn(lst):
    min_v = lst[0]  # 기본은 맨 앞
    for i in lst:  # 리스트 순회하면서
        if min_v > i:  # 큰값 만나면 값을 바꿈
            min_v = i
    return min_v


for tc in range(1, T+1):
    len_lst = int(input())
    lst = list(map(int, input().split()))
    ans = [0] * len_lst  # 받은 리스트 길이만큼의 새로운 리스트 생성

    for i in range(len_lst - 1):    # 0부터 끝 전까지
        for nxt_idx in range(i + 1, len_lst):  # 1부터 끝까지 비교
            if lst[i] > lst[nxt_idx]:  # 지금 비교하는 것보다 작은거 나오면
                ans[i] += 1    ## 지금 비교하는거 인덱스에 +1

    #print(ans)
    print(f'#{tc} {maxx(ans)}')

    pass

