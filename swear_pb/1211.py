import sys
sys.stdin = open("1211.txt")

for test_case in range(1, 11):
    t = int(input())

    ladder_lst = []
    for i in range(100):
        ladder_lst.append(list(map(int, input().split())))

    dx = [1,-1]
    dy = [0, 0]
    
    start_lst = []
    count_lst = []
    for i in range(100):  # 시작 위치 다 찾자
        if ladder_lst[0][i] == 1:
            start_lst.append(i)

    for start in start_lst:  # 시작 위치 다 검사
        curx = start
        cury = 0
        count = 0  # 이동 최소 구하려고 셈
        ## y, x 순
        while cury != 99:
            for j in range(2):  # 다시 왼오 검사
                end = True
                if (0 <= curx + dx[j] <=99) and ladder_lst[cury + dy[j]][curx + dx[j]] == 1:  # 갈 수 있으면
                    while end:  # 종료 조건 거짓일 떄까지
                        if (0 <= curx + dx[j] <=99) and ladder_lst[cury + dy[j]][curx + dx[j]] == 1:  # 계속 간다
                            curx += dx[j]
                            count += 1
                        else:
                            end = False  # 끝낸다
                    break
            cury += 1  # 내려가자
            count += 1
        count_lst.append(count)  # 다 내려갔으니 개수 매달음
    #print(count_lst.index(min(count_lst)))
    print(f'#{test_case} {start_lst[count_lst.index(min(count_lst))]}')  # 시작 리스트에서 이동거리 리스트에 최소값에 인덱스의 값 반환