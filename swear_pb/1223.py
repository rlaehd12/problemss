import sys
sys.stdin = open("1223.txt")

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


calculator = {'+': 1, '-': 1, '*': 2, '/': 2, None: 0}


def stack_cal(st, cal_st):
    cur_cal = st.pop()
    b = cal_st.pop()
    a = cal_st.pop()
    if cur_cal == '+': return cal_st.push(a+b)
    elif cur_cal == '*': return cal_st.push(a*b)
    elif cur_cal == '-': return cal_st.push(a-b)
    elif cur_cal == '/': return cal_st.push(a/b)


for tc in range(1, 11):
    n = int(input())
    lst = input()
    st = stack(n)  # 후위표기법으로 바꿀 스택, 밀어넣을 스택 바로 생성
    cal_st = stack(n)

    for word in lst:
        if word in calculator:
            if calculator[word] > calculator[st.peek()]:
                st.push(word)
            else:
                while calculator[word] <= calculator[st.peek()]:
                    stack_cal(st, cal_st)

                st.push(word)
        else:
            cal_st.push(int(word))
    
    while not st.isempty():
        stack_cal(st, cal_st)

    print(f'#{tc} {cal_st.peek()}')
