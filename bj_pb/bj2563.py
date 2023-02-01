import sys
sys.stdin = open('input2563.txt')

######### 겹치는개 여러부분인거 생각 못함
# lst = []
# sums = 0
# for i in range(int(input())):

#     m, n = map(int, input().split())
#     sums += 100

#     for j in range(len(lst)):
#         x1 = m
#         y1 = n
#         x2 = lst[j][0]
#         y2 = lst[j][1]

#         # print(10 + min(x1, x2) - max(x1, x2))
#         # print(10 + min(y1, y2) - max(y1, y2))

#         if ((10 + min(x1, x2) - max(x1, x2)) <= 0) or ((10 + min(y1, y2) - max(y1, y2)) <= 0):
#             continue
#         else:
#             sums -= (10 + min(x1, x2) - max(x1, x2)) * (10 + min(y1, y2) - max(y1, y2))


#     lst.append((m,n))

# print(sums)
##############이차원 배열에 칠하기

paper = [[0]*100 for i in range(100)]

for _ in range(int(input())):
    a,b = map(int,input().split())
    for i in range(10):
        for j in range(10):
            paper[a+i][b+j] = 1

r = 0
for i in paper:
    r += sum(i)
print(r)