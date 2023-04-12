def calculate():
    ans = lst[0]
    for i in range(N-1):
        if p[i] == 0:
            ans += lst[i+1]
        elif p[i] == 1:
            ans -= lst[i+1]
        elif p[i] == 2:
            ans *= lst[i+1]
        elif p[i] == 3:
            if ans >= 0:
                ans //= lst[i+1]
            else:
                ans = -(-ans//lst[i+1])
    return ans


def perm(i, k):
    if i == k:
        cur = calculate()
        ans[0] = max(ans[0], cur)
        ans[1] = min(ans[1], cur)
    else:
        for j in range(4):    # 사용하지 않은 숫자
            if operators[j] != 0:  # operators에서 순서대로 검색
                p[i] = j
                operators[j] -= 1  # j번 자리 숫자 사용했다 표시
                perm(i+1, k)
                operators[j] += 1  # j번 자리 원상복귀

N = int(input())
lst = list(map(int, input().split()))
operators = list(map(int, input().split()))
p = [0]*(N-1)
k = N-1
ans = [-float('inf'), float('inf')]  # 최대값, 최소값

perm(0, k)
for i in ans:
    print(i)