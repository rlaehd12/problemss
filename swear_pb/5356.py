import sys
sys.stdin = open("5356.txt")

t = int(input())

for tc in range(1,t+1):
    ########### 다른 풀이
    arr = [input() for _ in range(5)]
    # arr_t = list(zip(*arr)) 입력 가로세로가 다르면 전치 행렬 불가 zip 특성상
    ans = ''
    for j in range(15):
        for i in range(5):
            if j < len(arr[i]):
                ans += arr[i][j]
    
    print(f'#{tc} {ans}')

    ###########
    # lst = []
    # for _ in range(5):
    #     lst.append(input())

    # print(f'#{tc}', end=' ')

    # for j in range(15):
    #     for i in range(5):
    #         try: print(lst[i][j], end='')
    #         except: pass
    # print()
