import sys
sys.stdin = open("1219.txt")


for test_case in range(1, 11):
    t, e = map(int, input().split())
    arr = list(map(int, input().split()))
    elst = [[] for _ in range(100)]
    stack = [0]
    visited = [0] * 100
    visited[0] = 1
    
    for i in range(e):  # edge 저장
        elst[arr[2*i]].append(arr[2*i + 1])

    while stack:  # 스택 빌때까지
        for ver in elst[stack[-1]]:
            if visited[ver] == 0:
                visited[ver] = 1
                stack.append(ver)
                break
        else:
            stack.pop()

    print(f'#{test_case} {visited[99]}')