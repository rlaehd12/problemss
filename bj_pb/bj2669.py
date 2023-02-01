import sys
sys.stdin = open('input2669.txt')

width_lst = [[0]* 100 for i in range(100)]
rec_lst = ()

for i in range(4):
    rec_lst = (tuple(map(int, input().split())))
    #print(rec_lst)
    for row in range(rec_lst[0], rec_lst[2]):
        for col in range(rec_lst[1], rec_lst[3]):
            width_lst[row][col] = 1
    #         print(col, end=' ')
    #         print(row, end= ' ')
    #     print('')
    # print('')

# for i in range(20):

#     print(width_lst[i], end= '')
#     print('')

all_sum = 0
for i in range(100):
    all_sum += sum(width_lst[i])

print(all_sum)
