import sys
sys.stdin = open("input2798.txt")

n, m = map(int, input().split())  # n 카드 개수 # m 목표 숫자
card_lst = list(map(int, input().split()))

#print(card_lst)
my_lst = []
cnt = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            cnt += 1
            f = (card_lst[i],card_lst[j],card_lst[k])
            my_lst.append(f)
            pass

small = sum(my_lst[0])

for i in my_lst:
    d = m - sum(i)
    if d < small and d >= 0:
        small = d
        my_small = sum(i)

print(my_small)