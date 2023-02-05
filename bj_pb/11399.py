n = int(input())

lst = list(map(int, input().split()))

def counting(lst, numb, n):
    sort_lst = [0] * n
    count = [0] * (numb+1)
    for i in lst:
        count[i] += 1
        pass
    
    for i in range(numb):
        count[i+1] += count[i]
        pass

    for i in range(n):  # count[i]가 가진 값에 위치에 넣어야 함
        count[lst[i]] -= 1
        sort_lst[count[lst[i]]] = lst[i]
        pass

    return sort_lst

lst = counting(lst, 1000, n)
print(lst)

summ = 0

for i in range(n-1):
    summ += lst[i]
    lst[i+1] += lst[i]

print(summ + lst[-1])
