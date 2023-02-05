import sys
sys.stdin = open("1210.txt")


for test_case in range(1, 11):
    t = int(input())
    ladder_lst = []
    for i in range(100):
        ladder_lst.append(list(map(int, input().split())))

    curx = ladder_lst[99].index(2)
    cury = 99

    dx = [1,-1]
    dy = [0,0]


    ## y, x 순
    while cury != 0:
        for j in range(2):  # 다시 왼오 검사
            end = True
            if (0 <= curx + dx[j] <=99) and ladder_lst[cury + dy[j]][curx + dx[j]] == 1:  # 갈 수 있으면
                while end:  # 종료 조건 거짓일 떄까지
                    if (0 <= curx + dx[j] <=99) and ladder_lst[cury + dy[j]][curx + dx[j]] == 1:  # 계속 간다
                        curx += dx[j]
                    else:
                        end = False  # 끝낸다
                break
        cury -= 1  # 올라가자

    print(f'#{test_case} {curx}')
        