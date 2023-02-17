import sys
sys.stdin = open("5430.txt")


t = int(input())

for tc in range(1,t+1):
    order = input()
    n = int(input())
    lst = input()[1:-1].split(',')

    if n !=0:
        lst = list(map(int, lst))
    else:
        lst = []
    a = 0
    pos = [0, -1]
    for word in order:
        if word == 'R':
            a = (a+1)%2
        elif word == 'D':
            if lst:
                lst.pop(pos[a])
            else:
                print('error')    
                break
    else:
        if a == 0:
            print(lst)
            # print("[" + ",".join(iterable) + "]")
        else:
            lst.reverse()
            print(lst)
