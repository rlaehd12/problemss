# 1을 만날때 5~1까지 색종이를 넣고, 다음 색종이를 재귀로 탐색할거임

def dfs(a,b):  # 시작위치 지정
    flag = True
    for i in range(10):
        for j in range(10):
            if not (a == i and b == j) and flag == True:  # a, b도달할때까지 ㄱㄱ
                continue
            else:
                flag = False

            if lst[i][j] == 1:
                for width in range(5,0,-1):  # 5 ~ 1까지
                    if paper_lst.count(0) == 6:  # 종이 남은거 없으면 종료
                        return
                    if paper_lst[width] == 0:  # 종이 없으면 다음 종이
                        continue
                    elif nemo(i, j, width):
                        ans[1] += 1
                        if ans[0] <= ans[1]:  # backtracking
                            ans[1] -= 1
                            return

                        color(i, j, width)
                        paper_lst[width] -= 1

                        dfs(i, j+width-1)  # dfs 들어감

                        color(i, j, width, reverse=False)
                        paper_lst[width] += 1
                        ans[1] -= 1


            if i == 9 and j == 9:  # base case
                for p in range(10):
                    for q in range(10):
                        if lst[p][q] == 1:
                            return
                print(ans[1])
                if ans[0] > ans[1]:
                    ans[0] = ans[1]
                return

def nemo(i,j,width):  # 현 위치와 종이 크기 주면 네모 만들수 있는지 아닌지 ox로 출력
    for p in range(width):
        for q in range(width):
            ci = i+p
            cj = j+q
            if 0<=ci<10 and 0<=cj<10:
                if lst[ci][cj] == 1:
                    continue
                else:
                    return False
            else:
                return False
    return True

def color(i,j,width, reverse=True):  # reverse false -> 1로 다시 원상복귀함
    for p in range(width):
        for q in range(width):
            ci = i+p
            cj = j+q
            if reverse == True:
                lst[ci][cj] = 0
            else:
                lst[ci][cj] = 1
    return

import sys
sys.stdin = open("17136.txt")

lst = [list(map(int, input().split())) for _ in range(10)]
paper_lst = [0, 5, 5, 5, 5, 5]
ans = [100, 0]  # gloal ans, local ans
dfs(0, 0)
if ans[0] == 100:
    print(-1)
else:
    print(ans[0])
