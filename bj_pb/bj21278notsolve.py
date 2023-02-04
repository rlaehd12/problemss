import sys
sys.stdin = open("input21278.txt")

n, m = map(int, input().split())
road_lst = []  # 도로 리스트 
chicken_loc_lst = []  # 모든 가능 치킨집 리스트


for _ in range(m):
    road_lst.append(list(map(int, input().split())))

#print('road lst',road_lst)


for i in range(n-1):
    for j in range(i+1,n):
        chicken_loc_lst.append([i+1,j+1])

#print('chicken loc lst',chicken_loc_lst)
shortest = 100000
a = b = 0
for chicken in chicken_loc_lst:
    road_lst2 = road_lst[:]
    visited = [-1] * (n + 1)  # 계속 초기화 해줘야 할듯
    cur_loc = set(chicken)  # 초기 방문, 현재 위치는 집합
    count = 0

    while cur_loc:  # 비어있지 않으면
        cur_road = []
        for cur in cur_loc:  # 일단 방문 확인
            visited[cur] = count
        
        for visit in visited[1:]:  # 방문 다 했는지 확인
            if visit == -1:
                break
        else:
            print((sum(visited)+1)*2)
            if (shortest >(sum(visited)+1)*2):
                shortest = (sum(visited)+1)*2
                a, b = chicken
            break

        
        for cur in cur_loc:  # 갈수 있는 도로 확인
            for road in road_lst:
                if (cur in road) and (visited[road[road.index(cur)-1]] == -1):  # 도로연결되었고, 그 반대편이 아직 방문 안함
                    cur_road.append(road)
                    pass
        
        del_set = set(cur_loc)
        for road in cur_road:
            for r in road:
                cur_loc.add(r)
                pass
        cur_loc -= del_set  # 다음 방문을 위해 빼버림
        count += 1
        pass

print(a,b,shortest)
