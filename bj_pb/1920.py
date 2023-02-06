import sys
sys.stdin = open("1920.txt")

n = int(input())
lst1 = set(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))

for i in lst2:
    b = 1 if i in lst1 else 0
    print(b)