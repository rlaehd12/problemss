import sys
sys.stdin = open("4866.txt")

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

bracket = {'{':'}', '[':']', '(':')'}

for tc in range(1,t+1):

    check = 0
    words = input()
    st = stack(len(words))
    for word in words:
        if word == '{' or word == '[' or word == '(':
            st.push(word)
        elif word == '}' or word == ']' or word == ')':
            if word == bracket.get(st.peek()):
                st.pop()
            else:
                break
    else:  # 끝까지 브레이크 안걸리면
        if st.isempty():
            check = 1


    print(f'#{tc} {check}')
    pass