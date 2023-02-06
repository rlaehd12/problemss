import sys
sys.stdin = open("d3_1.txt")

t = int(input())

for test_case in range(1, t+1):
    n = int(input())

    # 상하좌우
    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))

    cnt = 0

    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i +di[k]
                nj = j +dj[k]
                if 0<=ni<n and 0<=nj<n:
                    #print(lst[ni][nj], end=' ')
                    cnt += abs(lst[i][j] - lst[ni][nj])
            #print()
    
    print(f'#{test_case} {cnt}')