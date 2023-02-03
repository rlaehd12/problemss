import sys
sys.stdin = open("input9367.txt")

t = int(input())
for test_case in range(1, t + 1):
    N = int(input())
    lst = input()

    #print(lst)
    ans = 0
    cnts = 0
    for i in range(len(lst)):
        if lst[i] == '0':
            cnts = 0
        else:
            cnts += 1
            if ans < cnts:
                ans = cnts


    print(f'#{test_case}', ans)