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

class heap(stack):  # 최소 힙 변형

    def __init__(self, n):
        super().__init__(n+1)
        self.top = 0
    
    def isempty(self):
        if self.top == 0:
            return True
        else:
            return False
    
    def enq(self, n):
        self.push(n)
        c = self.top
        p = c//2
        while p > 0 and self.lst[c][1] < self.lst[p][1]:
            self.lst[c], self.lst[p] = self.lst[p], self.lst[c]
            c = p
            p = c//2
    
    def deq(self):
        if self.isempty():
            return

        temp = self.lst[1]
        self.lst[1] = self.pop()

        p = 1
        c = p*2

        while c <= self.top:
            if c+1 <= self.top and self.lst[c][1] > self.lst[c+1][1]:
                c += 1
            
            if self.lst[c][1] < self.lst[p][1]:
                self.lst[c], self.lst[p] = self.lst[p], self.lst[c]
            else:
                break

            p = c
            c = p*2
        return temp


import sys
sys.stdin = open("11000.txt")

N = int(input())
h = heap(N)
lst = [tuple(map(int, input().split())) for _ in range(N)]
lst.sort()
cnt = 0
for cur in lst:
    if h.isempty():
        h.enq(cur)
    else:
        if h.lst[1][1] <= cur[0]:
            h.deq()
            h.enq(cur)
        else:
            h.enq(cur)
    if cnt < h.top:
        cnt = h.top

print(cnt)
