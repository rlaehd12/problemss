import sys
sys.stdin = open("2930.txt")

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

class heap(stack):  # 최대 힙

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
        while p > 0 and self.lst[c] > self.lst[p]:
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
            if c+1 <= self.top and self.lst[c] < self.lst[c+1]:
                c += 1
            
            if self.lst[c] > self.lst[p]:
                self.lst[c], self.lst[p] = self.lst[p], self.lst[c]
            else:
                break

            p = c
            c = p*2
        return temp



t = int(input())

for tc in range(1,1+t):
    n = int(input())
    h = heap(n)
    ans = []
    print(f'#{tc} ',end='')
    for _ in range(n):
        a,*b = map(int, input().split())
        if a == 1:
            h.enq(b[0])
        else:
            cur = h.deq()
            if cur == None:
                ans.append(-1)
            else:
                ans.append(cur)
    
    for i in ans:
        print(i, end=' ')
    print()