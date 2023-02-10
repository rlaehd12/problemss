import sys
sys.stdin = open("1989.txt")

def check(lst):
    lst_len = len(lst)
    for i in range(lst_len//2):
        if lst[i] == lst[-1-i]:
            continue
        else:
            return 0
    else:
        return 1

t = int(input())
for tc in range(1,t+1):
    lst = input()
    print(f'#{tc} {check(lst)}')
