from collections import deque

# def bfs():  # 느림
#     visited = [0]*(K)  # 방문한 버스
#     while q:
#         c = q.popleft()  # 현재 버스
#         if bus_lst[c][1] == bus_lst[c][3]:  # y move
#             left = min(bus_lst[c][2], bus_lst[c][4])
#             right = max(bus_lst[c][2], bus_lst[c][4])
#             for i in range(K):  # 다음 버스 찾기
#                 if visited[i] != 0:  # 이미 탔던 버스라면
#                     continue
#                 for cur in range(left, right+1):  # 현재 버스가 갈 수 있는 모든 위치 확인
#                     if can_go(i, bus_lst[c][1], cur):  # 현재 좌표가 다음 버스 탈 수 있스면
#                         visited[i] = visited[c]+1
#                         q.append(i)
#                         break
#         else:  # x move
#             left = min(bus_lst[c][1], bus_lst[c][3])
#             right = max(bus_lst[c][1], bus_lst[c][3])
#             for i in range(K):  # 다음 버스 찾기
#                 if visited[i] != 0:  # 이미 탔던 버스라면
#                     continue
#                 for cur in range(left, right+1):  # 현재 버스가 갈 수 있는 모든 위치 확인
#                     if can_go(i, cur, bus_lst[c][2]):  # 현재 좌표가 다음 버스 탈 수 있스면
#                         visited[i] = visited[c]+1
#                         q.append(i)
#                         break
#     return visited

def bfs():
    visited = [0]*(K)  # 방문한 버스
    for i in q:
        visited[i] = 1
    while q:
        c = q.popleft()  # 현재 버스
        flag = 0  # 0이면 y축 이동, 1이면 x축 이동
        if bus_lst[c][1] == bus_lst[c][3]:  # cur y move
            cleft = min(bus_lst[c][2], bus_lst[c][4])
            cright = max(bus_lst[c][2], bus_lst[c][4])
            flag = 0
            if cleft<=dy<=cright and dx == bus_lst[c][1]:
                return visited
        else:  # cur x move
            flag = 1
            cleft = min(bus_lst[c][1], bus_lst[c][3])
            cright = max(bus_lst[c][1], bus_lst[c][3])
            if cleft<=dx<=cright and dy == bus_lst[c][2]:
                return visited
        

        for i in range(K):
            if visited[i] != 0:
                continue
            else:
                if bus_lst[i][1] == bus_lst[i][3]:  # 다음 버스 y축 이동
                    if flag == 0:  # 나도 y축 이동
                        if bus_lst[i][1] != bus_lst[c][1]:  # 엑스 다르면 깨짐
                            continue
                        else:  # 범위가 겹치는지 확인
                            nleft = min(bus_lst[i][2], bus_lst[i][4])
                            nright = max(bus_lst[i][2], bus_lst[i][4])
                            if nleft<=cleft<=nright or cleft<=nleft<=cright:  # 둘중 하나라도 범위 겹치면
                                visited[i] = visited[c]+1
                                #==================================
                                if nleft<=dy<=nright and bus_lst[i][1]==dx:
                                    return visited
                                q.append(i)
                            else:
                                continue
                    else:  # 나는 x축 이동
                        if cleft<= bus_lst[i][1] <=cright:  # 만약에 내가 가는 곳에 다음 버스가 있을 수 있다면
                            nleft = min(bus_lst[i][2], bus_lst[i][4])
                            nright = max(bus_lst[i][2], bus_lst[i][4])
                            if nleft<=bus_lst[c][2]<=nright:
                                visited[i] = visited[c]+1
                                #==================================
                                if nleft<=dy<=nright and bus_lst[i][1]==dx:
                                    return visited
                                q.append(i)
                            else:
                                continue
                        else:
                            continue
                else:  # 다음 버스 x축 이동
                    if flag == 1:  # 나도 x축 이동
                        if bus_lst[i][2] != bus_lst[c][2]:  # 와이가 다르면 깨짐
                            continue
                        else:  # 범위가 겹치는지 확인
                            nleft = min(bus_lst[i][1], bus_lst[i][3])
                            nright = max(bus_lst[i][1], bus_lst[i][3])
                            if nleft<=cleft<=nright or cleft<=nleft<=cright:  # 둘중 하나라도 범위 겹치면
                                visited[i] = visited[c]+1
                                #==================================
                                if nleft<=dx<=nright and bus_lst[i][2]==dy:
                                    return visited
                                q.append(i)
                            else:
                                continue
                    else:  # 나는 y축 이동
                        if cleft<= bus_lst[i][2] <=cright:  # 만약에 내가 가는 곳에 다음 버스가 있을 수 있다면
                            nleft = min(bus_lst[i][1], bus_lst[i][3])
                            nright = max(bus_lst[i][1], bus_lst[i][3])
                            if nleft<=bus_lst[c][1]<=nright:
                                visited[i] = visited[c]+1
                                #===================================
                                if nleft<=dx<=nright and bus_lst[i][2]==dy:
                                    return visited
                                q.append(i)
                            else:
                                continue
                        else:
                            continue

    return visited

def can_go(i, x, y):  # i번 버스가 xy갈 수 있나
    if bus_lst[i][1] == x or bus_lst[i][2] == y:  # 같은 줄에 있으면
        if bus_lst[i][1] == bus_lst[i][3]:
            left = min(bus_lst[i][2], bus_lst[i][4])
            right = max(bus_lst[i][2], bus_lst[i][4])
            if left <= y <= right:
                return True
            else:
                return False
        else:
            left = min(bus_lst[i][1], bus_lst[i][3])
            right = max(bus_lst[i][1], bus_lst[i][3])
            if left <= x <= right:
                return True
            else:
                return False
        pass
    else:
        return False  # 같은 줄에 없으면 아예 못감

def find_start(sx,sy):
    s_lst = []
    for i in range(K):
        if can_go(i, sx, sy):
            s_lst.append(i)

    return s_lst


M, N = map(int, input().split())
K = int(input())
bus_lst = [list(map(int, input().split())) for _ in range(K)]
sx, sy, dx, dy = map(int, input().split())
q = deque(find_start(sx, sy))  # 시작점 모두 매달기
# print(q)
lst = bfs()
# print(lst)
print(max(lst))
