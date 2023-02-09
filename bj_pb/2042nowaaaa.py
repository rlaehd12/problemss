import sys
sys.stdin = open("2042.txt")

n, m, k = map(int, input().split())
lst = [0]
for i in range(n):
    lst.append(int(input()))

ch_lst = []
for i in range(m+k):
    ch_lst.append(tuple(map(int, input().split())))

pre_sum = []
n_sum = 0
for num in lst:
    n_sum += num
    pre_sum.append(n_sum)

# print(ch_lst)

for i in ch_lst:
    if i[0] == 1:
        for j in range(i[1], n+1):
            pre_sum[j] += (i[2] - lst[i[1]])
        lst[i[1]] = i[2]
        pass
    else:
        print(pre_sum[i[2]] - pre_sum[i[1]-1])
        pass
# print(lst)
# print(pre_sum)
