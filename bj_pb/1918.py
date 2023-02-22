import sys
sys.stdin = open("1918.txt")

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
            return
        else:
            return self.lst[self.top]


calculator = {'+': 1, '-': 1, '*': 2, '/': 2, None: -1}


lst = input()
st = stack(100)  # 후위표기법으로 바꿀 스택, 밀어넣을 스택 바로 생성
cal_st = stack(100)

for word in lst:
    if word in calculator:  # 연산자일때
        if st.peek() == '(' or calculator[word] > calculator[st.peek()]:
            st.push(word)
        else:
            while st.peek() != '(' and calculator[word] <= calculator[st.peek()]:
                # stack_cal(st, cal_st)
                cal_st.push(st.pop())

            st.push(word)
    elif word == '(':  # 왼쪽 괄호는 그냥 밀어넣음
        st.push(word)
    elif word == ')':  # 오른쪽 괄호일때
        while st.peek() != '(':
            # stack_cal(st, cal_st)
            cal_st.push(st.pop())
        st.pop()
    else:  # 그냥 숫자일때
        cal_st.push(word)

while not st.isempty():
    # stack_cal(st, cal_st)
    cal_st.push(st.pop())

for i in cal_st.lst:
    if i != 0:
        print(i,end='')
