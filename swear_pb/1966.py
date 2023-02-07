def bubble(lst, n):
    for i in range(n-1):
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

t = int(input())

for test_case in range(1,t+1):
    print(f'#{test_case}', end=' ')
    n = int(input())
    lst = list(map(int, input().split()))
    for i in bubble(lst, n):
        print(i, end=' ')
    print()
