import sys
sys.stdin = open("1259.txt")

while True:
    a = input()
    if a == '0':
        break
    for i in range(len(a)//2):
        if a[i] != a[-i-1]:
            print('no')
            break
    else:
        print('yes')