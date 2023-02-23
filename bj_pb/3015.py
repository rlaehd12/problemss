import sys
sys.stdin = open("3015.txt")

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

n = int(input())
lst = stack(n)
ans = 0
for i in range(n):
    now = int(input())
    while (lst.peek() != None) and (lst.peek()[0] < now):  # 큰거 왔으면
        cur_cnt = lst.pop()
        
        ans += cur_cnt[1]


    if lst.peek() == None:  # 없으면 추가
        lst.push((now, 1))
    elif lst.peek()[0] > now:  # 작으면 
        lst.push((now, 1))
        ans += 1
    else:  #  같은 키 오면
        cur_cnt = lst.pop()[1]
        lst.push((now, cur_cnt+1))
        ans += cur_cnt
        if lst.top-1 != -1:
            ans += 1

    # print(lst.lst[:lst.top+1], ans)

print(ans)
    