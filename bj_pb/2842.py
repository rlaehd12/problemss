import sys
sys.stdin = open("2842.txt")

di = (1,1,1,0,0,-1,-1,-1)
dj = (1,0,-1,1,-1,1,0,-1)

def bfs(si, sj):
    v = [[0]*n for _ in range(n)]
    q = [(si,sj)]
    v[si][sj] = 1
    if not scope[0] <= height[si][sj] <= scope[1]:  # 시작점이 범위 밖이면 끝
        return False

    while q:  # not empty
        ci, cj = q.pop(0)
        for i in range(8):  # 8 dir
            ni, nj = ci+di[i], cj+dj[i]
            if 0<=ni<n and 0<=nj<n and v[ni][nj] ==0:  # 방문 안했고 인덱스 안벗어나고
                if scope[0] <= height[ni][nj] <= scope[1]:  # 현재 범위 안에 있다면
                    q.append((ni,nj))
                    v[ni][nj] = 1
    
    for end in end_lst:
        if v[end[0]][end[1]] == 1:
            continue
        else:
            return False
    else:
        return True


n = int(input())
zido = []
height = []
end_lst = []
minmax = set()

for _ in range(n):
    zido.append(input())

for _ in range(n):
    height.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        minmax.add(height[i][j])
        if zido[i][j] == 'P':  # 시작점 찾기
            si, sj = (i,j)
        elif zido[i][j] == 'K':
            end_lst.append((i,j))

minmax = sorted(list(minmax))
h_length = len(minmax)
left = 0
right = 0
ans = 99999999999

while right < h_length:
    scope = (minmax[left], minmax[right])
    print(scope)
    if not bfs(si, sj):  # 모든 도착지 도착 못하면
        right += 1
    else:
        if ans > minmax[right] - minmax[left]:
            ans = minmax[right] - minmax[left]
        
        if left < right:
            left += 1
        else:
            right += 1

print(ans)