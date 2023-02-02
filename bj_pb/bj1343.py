xx = input()
mystr = ''
count = 0
for x in xx:
    #print(x)
    if x == 'X':
        count += 1
    else:
        if count % 2 == 1:
            break
        while count > 0:
            if count >=4:
                mystr += 'AAAA'
                count -= 4
            else:
                mystr += 'BB'
                count -= 2
        mystr += '.'

if count % 2 == 1:
    print(-1)
    exit()
while count > 0:
    if count >=4:
        mystr += 'AAAA'
        count -= 4
    else:
        mystr += 'BB'
        count -= 2


print(mystr)



