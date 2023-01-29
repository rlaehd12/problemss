import sys
sys.stdin = open('input2628.txt')

a, b = map(int, input().split())
n = int(input())
row_lst = [0, b]
col_lst = [0, a]
big_row = 0
big_col = 0

def long_len(lst):
    longg = 0
    for long in range(1,len(lst)):
        if longg < lst[long] - lst[long-1]:
            longg = lst[long] - lst[long-1]
    return longg

for i in range(n):
    m, n = map(int, input().split())
    if m == 0:
        row_lst.append(n)
    else:
        col_lst.append(n)

row_lst.sort()
col_lst.sort()


print(row_lst, col_lst)

r = long_len(row_lst)
c = long_len(col_lst)
print(r * c)