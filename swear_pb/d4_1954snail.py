# t = int(input())

# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]

# for test_case in range(1, t+1):
#     n = int(input())

#     lst = []  # 리스트
#     count = n-1  # 이동 거리
#     ni = 0  # 내 위치
#     nj = 0
#     lst.append((ni,nj))  # 맨 처음 위치 매달음
#     while count > 0:
#         for i in range(4):  # 4가지 방향
#             for j in range(count):
#                 if i != 3:  # 3번째까지는 그냥 감
#                     ni += di[i]
#                     nj += dj[i]
#                     lst.append((ni, nj))
#                 else:
#                     if count == 1:  # 1칸이면 더 갈데 없음
#                         break
#                     if j <= count-2:  # 마지막 -1 번째
#                         ni += di[i]
#                         nj += dj[i]
#                         lst.append((ni, nj))
#                     else:  # 마지막은 오른쪽으로 한칸
#                         ni += di[0]
#                         nj += dj[0]
#                         lst.append((ni, nj))
#         count -= 2
#     print_lst = [[0] * n for _ in range(n)]

#     for i in range(n**2):
#         print_lst[lst[i][0]][lst[i][1]] = i+1

#     print(f'#{test_case}')
#     for i in print_lst:
#         for j in i:
#             print(j, end=' ')
#         print()


# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def snail(x, y, N):
    # 시작점 == 1
    arr[x][y] = 1
    # 델타검색 우측부터 시작
    idx = 0
    # 2번째 값 == 2
    cnt = 2

    # N = 3 일때, 써내려간 수가 9가 될때까지
    while cnt <= N**2:
        # 델타 검색 좌표
        nx = x + dx[idx]
        ny = y + dy[idx]

        # N을 벗어나지 않고
        # 다음 조사 대상을 아직 방문하기 전이라면
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            # 해당 위치에 값 작성
            arr[nx][ny] = cnt
            # 다음 조사를 위해 내 현재 위치 변경
            x, y = nx, ny
            # 다음 위치에 적을 값 1증가
            cnt += 1
        # 4방향 우하좌상 모두 조사했다면
        elif idx == 3:
            # 다시 처음부터
            idx = 0
        # 아니라면
        else:
            # 다음 방향 조사
            idx += 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 최종 출력 위한 리스트
    arr = [[0]*N for _ in range(N)]

    # 조사 시작
    # 시작위치 (0,0)
    snail(0, 0, N)

    print(f'#{tc}')
    # 행,렬 순서대로 출력
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()