import sys
sys.stdin = open('input2491.txt')


for test in range(3): # 이거 그냥 테스트케이스 3개여서
    T = int(input())
    my_lst = list(map(int, input().split()))
    #print(my_lst)

    head = 0 # 대가리, 꼬리, 가장 큰 값 저장할 변수 정의
    tail = 0
    long_numb = 0

    while head <= T-3: # 대가리가 리스트 길이 -2까지 갈때까지
        # 일단 앞 뒤가 같으면 머리랑 꼬리 한칸씩 뒤로 물림
        if head > 0 and (my_lst[head] == my_lst[head-1]):
            head -= 1
            tail -= 1
            #print(head,tail, 'c')
            continue


        ############# 갈수록 계속 작아지면
        if my_lst[tail] > my_lst[tail+1]:
            tail += 1
            for i in range(len(my_lst[tail:])):
                if my_lst[tail] >= my_lst[1+tail]:# 계속 작아지면
                    #print(i, head, tail ,' b')
                    tail += 1
                    continue
                else: # 갑자기 커지면
                    if long_numb < tail - head + 1: # 저장된 값보다 길면 저장
                        long_numb = tail - head + 1
                        #print(head, tail,'a')
                        head = tail
                    else:
                        head = tail
                        break
                    break
        ########### 갈수록 계속 커지면
        elif my_lst[tail] < my_lst[tail+1]:
            tail += 1
            for i in range(len(my_lst[tail:])):
                if my_lst[tail] <= my_lst[1+tail]: #계속 커지면
                    tail += 1
                    continue
                else: # 갑자기 작아지면
                    if long_numb < tail - head + 1: # 저장된 값보다 길면 저장
                        long_numb = tail - head + 1
                        #print(head, tail)
                        head = tail
                    else:
                        head = tail
                        break
                    break
        ########## 앞에게 뒤에거랑 같으면
        else:
            tail += 1
            pass
    
    print(long_numb)