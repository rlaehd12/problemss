import sys
sys.stdin = open('input2491.txt')


for test in range(3): # 이거 그냥 테스트케이스 3개여서
    T = int(input())
    my_lst = list(map(int, input().split()))
    print(my_lst)
    head = 0 # 대가리, 꼬리, 가장 큰 값 저장할 변수 정의
    tail = 0
    long_numb = 0
    while head != T-2: # 대가리가 리스트 길이 -2까지 갈때까지
        ############# 앞에게 뒤에거보다 크면
        if my_lst[head] > my_lst[head+1]:
            tail += 1
            for i in range(len(my_lst[head+1:])):
                if my_lst[i] >= my_lst[i+1]:
                    tail += 1
                    continue
                else:
                    if long_numb < head - tail + 1:
                        long_numb = head - tail + 1
                    else:
                        break
                    break
        ########### 앞에게 뒤에거보다 작으면
        elif my_lst[head] < my_lst[head+1]:
            tail += 1
            for i in range(len(my_lst[head+1:])):
                if my_lst[i] <= my_lst[i+1]:
                    tail += 1
                    continue
                else:
                    if long_numb < head - tail + 1:
                        long_numb = head - tail + 1
                    else:
                        break
                    break
        ########## 앞에게 뒤에거랑 같으면
        else:
            pass
