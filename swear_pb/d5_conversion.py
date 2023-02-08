def itoaf(intt):
    strr = ''
    while intt >=1:
        a = intt % 10
        strr = f'{a}' + strr
        intt //= 10
    
    return strr

def itoa(intt):
    strr = ''
    um = False
    if intt != 0:
        if intt < 0:
            um = True
            intt = -intt

        while intt >=1:
            a = intt % 10
            intt //= 10
            for i in asci:
                if i[0] == a:
                    a = i[1]
                    break
            strr = chr(a) + strr
        
        if um:
            strr = '-' + strr

        return strr

    else:
        strr = '0'



asci = []
for i in range(10):
    a = f'{i}'
    asci.append((i, ord(a)))

print(itoaf(15234))
print(type(itoaf(321)))
print(itoa(15234))
print(type(itoa(321)))
print(itoa(-4123))
print(type(itoa(321)))

