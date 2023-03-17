import sys
sys.stdin = open("2206.txt")

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
s = (0,0)
e = (N-1, M-1)
print(maze)

def a():
    lst = [1,2,3]
    b(lst)
    print(lst)

def b(t):
    t[0] = 123

a()