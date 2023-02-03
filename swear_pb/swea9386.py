import sys
sys.stdin = open("input9386.txt")

t = int(input())
for test_case in range(1, t + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    #print(lst)
    ans = 0
    cnts = 0
    for i in range(N - 1):
        if lst[i] > lst[i+1]:
            cnts = 0
        else:
            cnts += 1
            if ans < cnts:
                ans = cnts


    print(f'#{test_case}', ans + 1)

