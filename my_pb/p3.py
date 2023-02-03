import sys
sys.stdin = open('input3.txt')

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}',end=' ')
    # m,n 리스트 길이 인풋받음
    m, n = map(int, input().split()) 
    # 리스트 2개 인풋받음
    list1 = input().split()
    list1 = list(map(int, list1))
    list2 = input().split()
    list2 = [int(i) for i in list2]
    # print(m,n)
    # print(list1, list2)

    trial = abs(m-n)+1
    big_sum = 0
    for i in range(trial):
        if m>n:
            #리스트 1이 2보다 크기가 크니까 2는 그대로, 1은 2의 크기만큼 이동하면서 곱셈
            ## 각각의 요소들을 zip으로 튜플로 묶고 그 둘의 곱을 리스트의 개수만큼 리스트에 저장함
            ### 그리고 리스트에 모든 요소를 sum으로 합함
            cur_sum = sum([ai * bi for ai, bi in zip(list2, list1[i:n+i])])
            #현재 루프에 곱셈 더한게 더 크면 과거 기록 갈아치우기
            if big_sum < cur_sum:
                big_sum = cur_sum

        elif m<n:
            #위와 같고 크기만 반대
            cur_sum = sum([ai * bi for ai, bi in zip(list2[i:m+i], list1)])
            if big_sum < cur_sum:
                big_sum = cur_sum

    print(big_sum)