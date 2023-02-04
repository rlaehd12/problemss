n = int(input())
m = n



cnt = 0

while m // 10 >=  1:
    m //= 10
    cnt += 1
# print(cnt)
if n > 20:  # 20이하일때 이상해져서 나누어서 품
    for i in range(10 ** cnt - (10 ** (cnt - 1)), n):  # 다 하면 시간 너무 오래걸리니까 범위 제한함
        #print(sum(map(int, str(i))))
        if sum(map(int, str(i))) + i == n:
            print(i)
            break
    else:
        print(0)
else:
    for i in range(n):
        if sum(map(int, str(i))) + i == n:
            print(i)
            break
    else:
        print(0)
        