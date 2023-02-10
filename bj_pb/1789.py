target = int(input())

i = 1
while True:
    comp = 0
    if i == 1:
        comp = 1
    elif i == 2:
        comp = 3
    elif i%2 == 1:
        comp = (i + 1) * (i//2) + (i+1)//2
    else:
        comp = (i + 1) * (i//2)
    
    if target < comp:
        print(i-1)
        break
    i+=1