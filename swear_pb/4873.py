import sys
sys.stdin = open("4873.txt")

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

for tc in range(1, t+1):
    lst = input()
    st = stack(len(lst))
    for word in lst:
        if st.peek() == word:
            st.pop()
        else:
            st.push(word)
    print(f'#{tc} {st.top + 1}')