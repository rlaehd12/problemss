import sys
sys.stdin = open("5177.txt")

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

class heap(stack):  # 최소 힙

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
        while p > 0 and self.lst[c] < self.lst[p]:
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
            if c+1 <= self.top and self.lst[c] > self.lst[c+1]:
                c += 1
            
            if self.lst[c] < self.lst[p]:
                self.lst[c], self.lst[p] = self.lst[p], self.lst[c]
            else:
                break

            p = c
            c = p*2
        return temp



t = int(input())

for tc in range(1,1+t):
    n = int(input())
    lst = list(map(int, input().split()))
    hp = heap(n)
    for numb in lst:  # 힙에 매달음
        hp.enq(numb)
    
    ans = 0
    t = hp.top
    t //= 2

    while t > 0:  # 조상노드 전부 순회함
        ans += hp.lst[t]
        t //= 2
    
    print(f'#{tc} {ans}')