R,C,W = map(int, input().split())
lst = [[1]*(i+1) for i in range(R+W-1)]
for i in range(1,R+W-1):
    for j in range(i+1):
        if j-1>=0 and j<=i-1:
            lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
# print(lst)
cnt = 0
cur = 0
for i in range(R-1,R+W-1):
    cur +=1
    flag = 0
    for j in range(i+1):
        if flag>=cur:
            break
        if j >=(C-1):
            cnt += lst[i][j]
            # print(lst[i][j], end=' ')
            flag += 1
    # print()
print(cnt)