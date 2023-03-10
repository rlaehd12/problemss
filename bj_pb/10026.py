import sys
sys.stdin = open("10026.txt")

di = (1,-1,0,0)
dj = (0,0,1,-1)

N = int(input())
lst = [input() for _ in range(N)]
visit = [[0]*N for _ in range(N)]