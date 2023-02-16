import sys
sys.stdin = open("4871.txt")

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

t = int(input())

for tc in range(1, 1+t):
    v, e = map(int, input().split())
    lst = [[] for _ in range(v+1)]  # vertex 수+1 만큼 생성
    # 인덱스에 있는 요소는 연결되어있는 정점
    for _ in range(e):
        a, b = map(int, input().split())
        lst[a].append(b)
    
    s, g = map(int, input().split())
    # 방문, 스택 초기화
    visited = [0]*(v+1)
    st = stack(v)
    st.push(s)
    visited[s] = 1

    while not st.isempty():  # 스택이 안비었으면
        for vertex in lst[st.peek()]:  # 스택 마지막 요소 돌면서
            if visited[vertex] == 0:
                st.push(vertex)
                visited[vertex] = 1
                break
        else:  # 스택 마지막거 연결할 곳 없으면
            st.pop()
    
    print(f'#{tc} {visited[g]}')