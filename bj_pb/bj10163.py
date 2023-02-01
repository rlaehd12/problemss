import sys
sys.stdin = open("input10163.txt")

n = int(input())

###### 시간초과됨#######
space = [[0]* 1010 for i in range(1010)]
big_row = 0
big_col = 0
paper_width_lst = [0] * (n+1)
for paper in range(1, n+1):
    p_lst = list(map(int, input().split()))
    #print(p_lst)
    if big_row < p_lst[0] + p_lst[2]:
        big_row = p_lst[0] + p_lst[2]
    if big_col < p_lst[1] + p_lst[3]:
        big_col = p_lst[1] + p_lst[3]
    for r in range(p_lst[0], p_lst[0] + p_lst[2]):
        for c in range(p_lst[1], p_lst[1] + p_lst[3]):
            space[r][c] = paper
    

for i in range(big_row):
    for j in range(big_col):
        #print(space[i][j], end=' ')
        paper_width_lst[space[i][j]] += 1
    #print('')

for i in paper_width_lst[1:]:
    print(i)