import sys
sys.stdin = open("5432.txt")

t = int(input())

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

# for tc in range(1,t+1):
#     laser = input()
#     st = stack(len(laser))

#     before = 0
#     cnt = 0
#     for point in laser:
#         if before == '(' and point == ')':  # 바로 (), 레이저 나온경우 현재 높이만큼 더해줌
#             cnt += st.top
#             st.pop()
#         elif point == '(':  # 그냥이면 push
#             st.push(point)
#         elif point == ')':  # 터뜨리고 +1
#             st.pop()
#             cnt += 1
#         before = point
#     print(f'#{tc} {cnt}')

## 다른 풀이

for tc in range(1,t+1):
    st = input()
    ans = 0
    cnt = 0

    for i in range(len(st)):
        if st[i] == '(': # 막대기 시작 또는 레이저
            cnt += 1
        else:
            if st[i-1] == '(':  # 레이저임
                cnt -= 1
                ans += cnt
            else:  # 막대기끝임
                cnt -= 1
                ans += 1


    print(f'#{tc} {ans}')