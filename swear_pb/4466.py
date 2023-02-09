import sys
sys.stdin = open("4466.txt")

t = int(input())

def counting(lst, n, biggest):
    count = [0] * (biggest+1)
    return_lst = [0] * n
    for i in range(n):  # 세기
        count[lst[i]] += 1
    
    return count  # 더 필요 없을듯
    
    for i in range(biggest):  # 누적합
        count[i+1] += count[i]



for tc in range(1,t+1):
    n, k = map(int, input().split())
    nlst = list(map(int, input().split()))
    print(nlst)
    ans = 0
    cc = counting(nlst, n, 100)
    cc = cc[::-1]

    for i in range(k):
        for k in range(100):
            if cc[k] != 0:
                cc[k] -= 1
                ans += (100-k)
                break
    
    print(f'#{tc} {ans}')

    pass