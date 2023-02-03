lst_len = int(input())
n = int(input())
t = input()

idx = 0
cnt = 0
cur = 2

while cnt < n:
    plus_str = cur * '0' + cur * '1'
    cur_str = f'0101{plus_str}'

    for word in cur_str:
        idx += 1
        if word == t:
            cnt += 1
            if cnt == n:
                break
        


    cur += 1

print((idx-1) % lst_len)