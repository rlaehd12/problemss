##숫자 배열 회전시키기
import sys
sys.stdin = open('1961.txt')

def round90(list2,length):
    roundlist = [[] for i in range(length)]
    for i in range(length-1,-1,-1):
        for j in range(length):
            roundlist[j].append(list2[i][j])
    return roundlist


T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}')

    N = int(input()) # 리스트 크기 받기
    arr = [[] for i in range(N)] # 2차원 리스트 생성 및 데이터 받기
    for i in range(N): 
        arr[i] = input().split()

    list90 = round90(arr, N)
    list180 = round90(list90, N)
    list270 = round90(list180, N)

    # for i in range(N): # 보기 헷갈려서 보기 편하게 출력
    #     print(list180[i])

    for i in range(N):
        for j in list90[i]:
            print(j,end='')
        print(' ', end='')
        for j in list180[i]:
            print(j,end='')
        print(' ', end='')
        for j in list270[i]:
            print(j,end='')
        
        print('')

    # 다른 풀이
    
    a1 = [[0]*N for _ in range(N)]
    a2 = [[0]*N for _ in range(N)]
    a3 = [[0]*N for _ in range(N)]

    # [1] 회전각도에 따른 위치값 저장
    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N-1-j][i]
            a2[i][j] = arr[N-1-i][N-1-j]
            a3[i][j] = arr[j][N-1-i]
    
    # 출력하기
    for a,b,c in zip(a1,a2,a3):
        # print(f'{"".join(a)} {"".join(b)} {"".join(c)}')
        pass

    for a in zip(a1,a2,a3):
        print(a)

    # # [2] 전치배열과 읽는 방향에 따른 처리
    # print(f'#{test_case}')
    # for i in range(N):
    #     print(f'{"".join(arr_t[i][::-1])} {"".join(arr[N-1-i][::-1])} {"".join(arr_t[N-1-i])}')