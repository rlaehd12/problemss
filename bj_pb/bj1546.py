n = int(input())
lst = tuple(map(int, input().split()))
lst = tuple(map(lambda x: (x/max(lst)) * 100, lst))
print(sum(lst)/n) 