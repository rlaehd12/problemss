import sys
sys.stdin = open("4836.txt")

t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    paper = [[0]*10 for _ in range(10)]  # 종이 하나 만듬
    color_lst = []
    for i in range(n):
        color_lst.append(list(map(int, input().split())))
    
    #print(color_lst)
    for col in color_lst:
        for i in range(col[0], col[2]+1):
            for j in range(col[1], col[3]+1):
                if paper[i][j] == 0 or paper[i][j] == col[4]:
                    paper[i][j] = col[4]
                else:
                    paper[i][j] = 3
    
    # for i in range(10):
    #     print(paper[i])
    # print()
    count = 0
    for i in range(10):
        for a in paper[i]:
            if a == 3:
                count += 1
    
    print(f'#{test_case} {count}')