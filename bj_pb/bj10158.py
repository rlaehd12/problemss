import sys
sys.stdin = open('input10158.txt')

row, col = map(int, input().split())
ax, ay = map(int, input().split())
t = int(input())

# 포문 하나인데 느리다고 함
# x_dir = 1
# y_dir = 1
# for i in range(t):
#     if ax == row:
#         x_dir = -1
#     elif ax == 0:
#         x_dir = 1
    
#     if ay == col:
#         y_dir = -1
#     elif ay == 0:
#         y_dir = 1
#     ax += x_dir
#     ay += y_dir
#     #print(ax, ay)
#     pass
# print(ax, ay)

# print(t-row+ax)
# print(t-col+ay)

# print('몫')
# print((t-row+ax)//row) # 몫
# print((t-col+ay)//col)

# print('나머지')
# print((t-row+ax)%row) # 나머지
# print((t-col+ay)%col)

if ((t-row+ax)//row) % 2==1:
    ax = (t-row+ax)%row
else:
    ax = row - (t-row+ax)%row


if ((t-col+ay)//col) % 2==1:
    ay = (t-col+ay)%col
else:
    ay = col - (t-col+ay)%col

print(ax, ay)