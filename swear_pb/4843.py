import sys
sys.stdin = open("4843.txt")

def selection(lst, n):
    for i in range(n-1):
        mini = i  # 최소 인덱스 정의
        for j in range(i+1, n):  # 최소 인덱스 계속 찾기
            if lst[mini] > lst[j]:  
                mini = j
        lst[mini], lst[i] = lst[i], lst[mini]
    
    return lst

t = int(input())

for test_case in range(1,t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    selection(lst, n)

    print(f'#{test_case}', end=' ')

    if n%2 == 0:
        left = lst[-1:(n//2)-1:-1]
        right = lst[0:(n//2)]
    else:
        left = lst[-1:(n//2)-1:-1]
        right = lst[0:(n//2)].append('')

    for i in range(5):
        print(left[i], right[i], end=' ')
    print()