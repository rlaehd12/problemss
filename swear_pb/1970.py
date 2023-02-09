t = int(input())

won_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1,t+1):
    a = int(input())
    ans = [0] * 8
    for i in range(8):
        while a // won_lst[i] > 0:
            ans[i] += a // won_lst[i]
            a -= won_lst[i] * (a // won_lst[i])
    print(f'#{tc}')
    for i in ans:
        print(i,end=' ')
    print()