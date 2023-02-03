##숫자 배열 회전시키기
import sys
sys.stdin = open('input2.txt')

def round90(list2,length):
    roundlist = [[] for i in range(length)]
    for i in range(length-1,-1,-1):
        for j in range(length):
            roundlist[j].append(list2[i][j])
    return roundlist


T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}')

    len_list = int(input()) # 리스트 크기 받기
    main_list = [[] for i in range(len_list)] # 2차원 리스트 생성 및 데이터 받기
    for i in range(len_list): 
        main_list[i] = input().split()

    list90 = round90(main_list, len_list)
    list180 = round90(list90, len_list)
    list270 = round90(list180, len_list)

    # for i in range(len_list): # 보기 헷갈려서 보기 편하게 출력
    #     print(list180[i])

    for i in range(len_list):
        for j in list90[i]:
            print(j,end='')
        print(' ', end='')
        for j in list180[i]:
            print(j,end='')
        print(' ', end='')
        for j in list270[i]:
            print(j,end='')
        
        print('')