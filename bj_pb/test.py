lst = list(map(int, input().split()))
before = lst[0]
cnt = 0
for i in lst[1:]:
    if before < i:
        cnt += 1
    before = i
if cnt == 7:
    print('ascending')
elif cnt == 0:
    print('descending')
else:
    print('mixed')