import sys
sys.stdin = open("1966.txt")

t = int(input())
for test_case in range(1, t+1):
    n, where = map(int, input().split())
    lst = list(map(int, input().split()))
    where_lst = [i for i in range(n)]
    #print(where, lst)
    count = 0
    while lst:
        if lst[0] < max(lst):
            lst.append(lst[0])
            where_lst.append(where_lst[0])
            lst.pop(0)
            where_lst.pop(0)
        else:
            lst.pop(0)
            count += 1
            if where_lst.pop(0) == where:
                print(count)
