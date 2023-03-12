import sys
sys.stdin = open("11812.txt")

N, K, Q = map(int, input().split())
const = K-2
lst = []
if K == 1:
    for _ in range(Q):
        a,b = map(int, input().split())
        lst.append(max(a, b) - min(a, b))
else:
    for _ in range(Q):
        a,b = map(int, input().split())
        cnt = 0
        # a큰거, b작은거
        while a != b:  # 둘이 같아질 때까지
            if a<b:
                a,b = b,a
            a = (a+const)//K
            cnt += 1
        lst.append(cnt)

for i in lst:
    print(i)
        