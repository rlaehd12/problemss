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
    if (lst.peek() == None) or (lst.peek() >= now):
        lst.push(now)
    else:
        while not lst.isempty() and lst.peek() <= now:
            lst.pop()
        lst.push(now)

    