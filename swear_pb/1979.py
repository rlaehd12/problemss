import sys
sys.stdin = open("1979.txt")

t = int(input())

for test_case in range(1, t+1):
    n, k = map(int, input().split())

    lst = []  # 가로방향 리스트
    for i in range(n):
        lst.append(list(map(int, input().split())))

    revlst = [[0]*n for _ in range(n)]  # 세로 방향 리스트

    for i in range(n):
        for j in range(n):
            revlst[i][j] = lst[j][i]
    
    cnt = 0

    for i in range(n):              # 세로 n칸 해야되니까
        for j in range(n-k+1):      # 가로 n-k+ 1 만큼 검사해야되니까
            for check in range(k):      # 하나 고르면 뒤 k개 검사
                if lst[i][j+check] == 0:
                    break
            else:     # k개 다 1이었으면 앞 뒤 검사
                if (j-1) >= 0 and (j+k) < n:  # 내부에 있으면
                    if lst[i][j-1] ==1 or lst[i][j+k] == 1: pass
                    else: cnt += 1
                elif (j-1) < 0:  # 왼쪽 끝
                    if lst[i][j+k] == 1: pass
                    else: cnt += 1
                else: #오른쪽 끝
                    if lst[i][j-1] ==1: pass
                    else: cnt += 1


    # 위랑 똑같이 진행
    for i in range(n):
        for j in range(n-k+1):     
            for check in range(k):      
                if revlst[i][j+check] == 0:
                    break
            else:     # k개 다 1이었으면 앞 뒤 검사
                if (j-1) >= 0 and (j+k) < n:  # 내부에 있으면
                    if revlst[i][j-1] ==1 or revlst[i][j+k] == 1: pass
                    else: cnt += 1
                elif (j-1) < 0:  # 왼쪽 끝
                    if revlst[i][j+k] == 1: pass
                    else: cnt += 1
                else: #오른쪽 끝
                    if revlst[i][j-1] ==1: pass
                    else: cnt += 1
    
    print(f'#{test_case} {cnt}')
