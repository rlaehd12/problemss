import sys
sys.stdin = open("17135.txt")

n, m, d = map(int, input().split())

lst = []
archer = [i for i in range(m)]
distance_lst = [[] for _ in range(m)]  # i, j, 거리순으로 저장할거임

for _ in range(n):
    lst.append(list(map(int, input().split())))

print(archer)
lst = lst[::-1]
for i in lst:
    print(i)

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            for k in range(m):
                distance_lst[k].append((i,j, i+1 + abs(j-k)))  # j가 가장 작은 순으로 죽임, 거리 측정

print(distance_lst)