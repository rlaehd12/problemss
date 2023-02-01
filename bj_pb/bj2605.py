import sys
sys.stdin = open('input2605.txt')

n = int(input())
numb_lst = map(int, input().split())
line_lst = []
count = 1
for i in numb_lst:
    line_lst.insert(i, count)
    count += 1

line_lst.reverse()

for i in line_lst:
    print(i, end=' ')