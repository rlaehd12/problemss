import sys
sys.stdin = open("input10163.txt")

# n = int(input())

# ###### 시간초과됨#######
# space = [[0]* 1010 for i in range(1010)]
# big_row = 0
# big_col = 0
# paper_width_lst = [0] * (n+1)
# for paper in range(1, n+1):
#     p_lst = list(map(int, input().split()))
#     #print(p_lst)
#     if big_row < p_lst[0] + p_lst[2]:
#         big_row = p_lst[0] + p_lst[2]
#     if big_col < p_lst[1] + p_lst[3]:
#         big_col = p_lst[1] + p_lst[3]
#     for r in range(p_lst[0], p_lst[0] + p_lst[2]):
#         for c in range(p_lst[1], p_lst[1] + p_lst[3]):
#             space[r][c] = paper
    

# for i in range(big_row):
#     for j in range(big_col):
#         #print(space[i][j], end=' ')
#         paper_width_lst[space[i][j]] += 1
#     #print('')

# for i in paper_width_lst[1:]:
#     print(i)

N = int(input())    # 색종이 장수
board = [[0] * 20 for _ in range(20)]
# 좌표 확인 리스트
cordinate = []
for k in range(N):
    x, y, w, h = map(int, input().split())  # 왼쪽 아래 좌표, 너비/높이
    cordinate.append([x, y, w, h])
    for i in range(x, x+w):
        for j in range(y, y+h):
            board[j][i] = k    # 가로 세로 바꼈다고 생각하고 좌표 배정

for i in board:
    print(i)

# 색종이 면적 구하기
for i in range(N):
    cnt = 0     # 색종이 면적
    x, y, w, h = cordinate[i]   # 1번 색종이에 대하여
    for p in range(x, x+w):
        for q in range(y, y+h):
            if board[q][p] == i:  # i랑 같으면 세줌
                cnt += 1
    print(cnt)