t = int(input())

for tc in range(1, t+1):
    N, Q = map(int, input().split())  # N개의 상자, Q번 반복

    box_lst = [0] * N

    for i in range(Q):  # L 부터 R 번까지 상자를 i로 값 변경
        L, R = map(int, input().split())
        L -= 1  # 인덱스 땜에 헷갈려서
        R -= 1

        for j in range(L,R+1):
            box_lst[j] = i+1
    print(f'#{tc}', end=' ')
    for i in box_lst:
        print(i, end= ' ')
    print('')