import sys
sys.stdin = open("4874.txt")

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

def stack_cal(st, word):
    b = st.pop()
    a = st.pop()
    if word == '+': return st.push(a+b)
    elif word == '*': return st.push(a*b)
    elif word == '-': return st.push(a-b)
    elif word == '/': return st.push(a/b)

for tc in range(1,t+1):
    lst = input().split()
    n = len(lst)
    st = stack(n)
    for word in lst:
        if word.isdigit():
            st.push(int(word))
        elif word == '.':
            pass
        else:
            if st.top >= 1:
                stack_cal(st, word)
            else:
                st.push('error')
                break

    if st.top >= 1:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {st.peek()}')