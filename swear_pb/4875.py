import sys
sys.stdin = open("4875.txt")

class stack():

    def __init__(self, n):
        self.lst = [0] * n
        self.top = -1
        self.size = n
    
    def isempty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def push(self, item):
        self.top += 1
        self.lst[self.top] = item
    
    def pop(self):
        if self.isempty():
            pass
        else:
            self.top -= 1
            return self.lst[self.top + 1]
    
    def peek(self):
        if self.isempty():
            pass
        else:
            return self.lst[self.top]

def find_path(lst, cur):
    st = []
    st.append(cur)
    while st:  # 스택이 빌때까지
        now = st.pop()
        for i in range(4):  # 4 방향 확인
            ni = now[0] + di[i]
            nj = now[1] + dj[i]
            if 0 <= ni < n and 0 <= nj < n:
                if lst[ni][nj] == 0:  # 갈 수 있으면 스택에 매달기, 1로 변경
                    st.append([ni, nj])
                    lst[ni][nj] = 1
                elif lst[ni][nj] == 3:  # 도착하면 종료
                    return 1

    return 0

t = int(input())
di = [1,-1,0,0]
dj = [0,0,1,-1]

for tc in range(1,t+1):
    n = int(input())

    lst = [[] for _ in range(n)]

    for i in range(n):
        for j in input():
            lst[i].append(int(j))

    # lst2 = []
    # for i in range(n):
    #     lst2.append(input())
    
    # for i in range(n):
    #     for j in range(n):
    #         lst[i].append(int(lst2[i][j]))


    for i in range(n):  # 시작점 위치 찾기
        for j in range(n):
            if lst[i][j] == 2:
                cur = [i, j]
                break
    
    print(f'#{tc} {find_path(lst, cur)}')