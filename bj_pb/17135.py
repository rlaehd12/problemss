import sys
sys.stdin = open("17135.txt")

def gen_combinations(arr, n):
    result =[] 

    if n == 0: 
        return [[]]

    for i in range(0, len(arr)): 
        elem = arr[i] 
        rest_arr = arr[i + 1:] 
        for C in gen_combinations(rest_arr, n-1): 
            result.append([elem]+C) 
              
    return result


n, m, d = map(int, input().split())

lst = []
archer = [i for i in range(m)]
distance_lst = [[] for _ in range(m)]  # i, j, 거리순으로 저장할거임

for _ in range(n):
    lst.append(list(map(int, input().split())))

# print(archer)
lst = lst[::-1]
# for i in lst:
#     print(i)

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            for k in range(m):
                distance_lst[k].append((i,j, i+1 + abs(j-k)))  # j가 가장 작은 순으로 죽임, 거리 측정

for i in range(m):
    distance_lst[i].sort(key=lambda x: x[1])
    distance_lst[i].sort(key=lambda x: x[2])
# print(distance_lst)
curarcher = gen_combinations(archer, 3)
biggest_cnt = 0
for tower in curarcher:  # 모든 궁수 조합
    cnt = 0
    killed = [[0]*m for _ in range(n)]
    for turn in range(n):  # n턴만큼 진행
        cankill = []
        for man in tower:  # 그중 한명
            for enemy in distance_lst[man]:
                if enemy[2]-turn <= d and enemy[0] >= turn and killed[enemy[0]][enemy[1]] == 0:  ## 아직 안죽었고// 동시에 죽일수도 있음## 사거리 되고 턴 안지났으면
                    cankill.append((enemy[0], enemy[1]))
                    break
        
        ### 죽은 사람 체크
        for samang in cankill:
            if killed[samang[0]][samang[1]] != 1:
                killed[samang[0]][samang[1]] = 1
                cnt += 1
    if biggest_cnt < cnt:
        biggest_cnt = cnt

print(biggest_cnt)