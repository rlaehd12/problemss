N = int(input())
cnt = 0
while N >= 0:
    if N%5 == 0:
        print(N//5+cnt)
        break
    N -= 3
    cnt += 1
else:
    print(-1)