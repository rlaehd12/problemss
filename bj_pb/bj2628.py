import sys
sys.stdin = open('input2628.txt')

a, b = map(int, input().split())
n = int(input())
row_lst = [0, b] # 행 리스트
col_lst = [0, a] # 열 리스트
big_row = 0 # 가장 큰 행
big_col = 0 # 가장 큰 열

def long_len(lst): # 리스트에서 가장 긴거 찾기 함수
    longg = 0
    for long in range(1,len(lst)):
        if longg < lst[long] - lst[long-1]:
            longg = lst[long] - lst[long-1]
    return longg

# 받는 족족 매달기
for i in range(n):
    m, n = map(int, input().split())
    if m == 0:
        row_lst.append(n)
    else:
        col_lst.append(n)

# 정렬
row_lst.sort()
col_lst.sort()


print(row_lst, col_lst)

# 함수에 넣어서 가장 긴거 찾고 곱하기
r = long_len(row_lst)
c = long_len(col_lst)
print(r * c)