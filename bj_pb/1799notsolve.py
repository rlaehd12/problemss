import sys
sys.stdin = open("1799.txt")

n = int(input())
right_check = [0] * ((2*n)-1)  # 대각선 방향 체크
left_check = [0] * ((2*n)-1)

lst = []
check_lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

cnt = 0
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:  # 놓을 수 있는지 확인
            check_lst.append((i+j, i + n-1 - j))

for chk in check_lst:
    pass

print(check_lst)
print(cnt)