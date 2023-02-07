import sys
sys.stdin = open("2001.txt")

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())

    paris = []  # 파리 리스트 2차원
    for i in range(n):
        paris.append(list(map(int, input().split())))

    kill_count = 0

    for row in range(n-m+1):  # 범위 나가지 않게 전부 다 검사함
        for col in range(n-m+1):
            kda = 0
            for i in range(m):      # m 크기 정사각형만큼    
                for j in range(m):  # 다 죽임
                    kda += paris[row+i][col+j]
            if kill_count < kda:
                kill_count = kda
    
    print(f'#{test_case} {kill_count}')