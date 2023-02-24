def solution(n):
    lst = [[0]*i for i in range(1,n+1)]
    idx = 1
    depth = 0
    answer = []
    while n>= 1:
        for i in range(n):
            lst[i+2*depth][depth] = idx
            idx += 1
        for i in range(n-1):
            lst[n-1+2*depth][depth+1+i] = idx
            idx += 1
        for i in range(n-2):
            lst[n-2-i+2*depth][n-2-i+2*depth-depth] = idx
            idx += 1
        depth += 1
        n -= 3
        print(lst)

    for i in lst:
        answer += i
    return answer

solution(7)
