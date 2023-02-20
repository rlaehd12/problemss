import sys
sys.stdin = open("5099.txt")

t = int(input())

for tc in range(1,t+1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    rotation = [0] * n
    ans_lst = [0] * n

    idx = 0
    i = 0
    while True:
        rotation[i] //= 2  # 한바퀴 돌면 반으로 나눔
        cnt = 0

        if idx == m:  # 개수 셈
            for numb in rotation:
                if numb == 0:
                    cnt += 1

        if rotation[i] == 0 and idx != m:  # 0이 되고 아직 피자 전부 안넣었으면
            ans_lst[i] = idx+1
            rotation[i] = lst[idx]
            idx += 1
        
        elif cnt == n-1:  # 마지막 피자만 남았으면
            # print(rotation, ans_lst)
            break
        i = (i+1) % n


    ans_idx = 0
    for i in range(n):  # 마지막 피자 위치 찾음
        if rotation[i] != 0:
            ans_idx = i
            break
    print(f'#{tc} {ans_lst[ans_idx]}')
