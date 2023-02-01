import sys
sys.stdin = open('input2559.txt')

N, K = map(int, input().split())

lst = list(map(int, input().split()))
big_num = 0
#print(lst)

######### sum 호출하느라 시간이 엄청 오래 걸림

# for i in range(N-K+1):
#     #print(lst[i:i+K])
#     if big_num < sum(lst[i:i+K]):
#         big_num = sum(lst[i:i+K])

print(sum(lst[:K]))

cur_sum = sum(lst[:K])
big_num = cur_sum
for i in range(N - K):
    cur_sum += (lst[K+i] - lst[i])
    if cur_sum > big_num:
        big_num = cur_sum
print(big_num)