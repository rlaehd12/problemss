import sys
#sys.stdin = open('input2635.txt')

big_num = 0
big_lst = []
n = int(input())

if n == 2:
    big_lst = [2, 1, 1, 0, 1]
    big_num = 5
else:
    for i in range(n//2 + 1,n+1):
        lst = [n, i]
        while lst[-2] - lst[-1] >= 0:
            lst.append(lst[-2] - lst[-1])
        if big_num < len(lst):
            big_num = len(lst)
            big_lst = lst[:]

print(big_num)
for i in big_lst:
    print(i, end=' ')
