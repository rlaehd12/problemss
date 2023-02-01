import sys
sys.stdin = open('input1244.txt')

T = int(input())#스위치 몇개인지 받음
sw_list = [] # 스위치 리스트 생성
sw_list = input().split()



students = int(input()) # 학생수 받음

def turn_ma(lst, obj): #남자일때
    idx = obj-1        #인덱스값은 목표-1
    for switch in lst[obj-1::obj]: # 목표-1부터 끝까지 목표만큼 스텝 뛰면서
        if switch == '0': # 스위치 키고 끄기
            lst[idx] = '1'
        else:
            lst[idx] = '0'
        idx += obj       # 인덱스 증가

    return lst[obj-1::obj]

def turn_fe(lst, obj): #여자일때
    idx = obj -1 # 인덱스값
    count = 1    # 앞뒤 확인용
    if lst[idx] == '0': # 일단 목표 스위치 키고 끄기
        lst[idx] = '1'
    else:
        lst[idx] = '0'

    while (idx-count >= 0) and (idx+count <= len(lst)-1) and (lst[idx+count] == lst[idx-count]):#주위인데 0보다는 크고 리스트보다는 작은 인덱스 값 가져야 함
        # 어차피 앞쪽 끝나면 뒤쪽 무시함

        if lst[idx+count] == '0': #목표 주위 스위치 키고 끄기
            lst[idx+count] = '1'
            lst[idx-count] = '1'
        else:
            lst[idx+count] = '0'
            lst[idx-count] = '0'
        count += 1 #더 큰 앞뒤 확인

    return lst

for student in range(students): # 학생수만큼
    p, s = map(int, input().split()) # 남녀, 몇번 스위치 확인
    if p == 1: #남자면
        turn_ma(sw_list, s)
        pass
    else:      #여자면
        turn_fe(sw_list, s)
        pass

countt = 0
for i in range(len(sw_list)):#리스트 원소 출력
    countt += 1
    print(sw_list[i], end=' ')
    if countt % 20 ==0:
        print('')