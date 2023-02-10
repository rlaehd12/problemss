import sys
sys.stdin = open("3055.txt")

row, col = map(int, input().split())

di = [1,-1,0,0] # 하 상 우 좌
dj = [0,0,1,-1]

old_lst = []
for i in range(row):
    old_lst.append(input())

# str 못바꾸니까 다 숫자로 바꿈
# 0 비어있음, 1 시작, 2 비버, 3 물, 4 돌

lst = [[0]*col for _ in range(row)]
for i in range(row):
    for j in range(col):
        if old_lst[i][j] == '.':
            lst[i][j] = 0
        elif old_lst[i][j] == 'S':
            lst[i][j] = 1
        elif old_lst[i][j] == 'D':
            lst[i][j] = 2
        elif old_lst[i][j] == '*':
            lst[i][j] = 3
        else:              # 돌 X
            lst[i][j] = 4

cnt = 0
end = False
while not end:
    water_lst = []
    gosum_lst = []
    for i in range(row):
        for j in range(col):
            if lst[i][j] == 3:
                water_lst.append((i,j))
            elif lst[i][j] == 1:
                gosum_lst.append((i,j))
    
    if not gosum_lst:  # 고슴도치 전멸
        print("KAKTUS")
        exit()
        end = True
        continue


    for water in water_lst:
        for k in range(4):  # 4 방향
            ni = water[0] + di[k]
            nj = water[1] + dj[k]
            if 0<= ni < row and 0<= nj < col:  # 물 범위 안에 있고
                if lst[ni][nj] != 2 and lst[ni][nj] != 4:
                    lst[ni][nj] = 3
    for gosum in gosum_lst:
        for k in range(4):  # 4 방향
            ni = gosum[0] + di[k]
            nj = gosum[1] + dj[k]
            if 0<= ni < row and 0<= nj < col:  # 고슴 범위 안에 있고
                if lst[ni][nj] == 0:
                    lst[ni][nj] = 1
                elif lst[ni][nj] == 2:
                    end = True
    cnt += 1



print(cnt)