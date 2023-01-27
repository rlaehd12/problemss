import sys
sys.stdin = open('input2116.txt')

def next_numb(numb): # 주사위 면 반대편 확인
    if numb == 0:
        return 5
    elif numb == 1:
        return 3
    elif numb == 2:
        return 4
    elif numb == 3:
        return 1
    elif numb == 4:
        return 2
    else:
        return 0

def big_number(numb1, numb2): # 양 면에 포함되지 않는 가장 큰 수
    if numb1 + numb2 == 11: # 6 5 주면
        return 4
    elif (numb1 == 6) or (numb2 == 6): #둘중 하나 6이면
        return 5
    else:
        return 6


######## 입력받기 string
T = int(input())

dice_lst = [] 
for dice in range(T):
    dice = input().split()
    dice_lst.append(dice)

########index 0 = 5 /// 1 = 3 /// 2 = 4
biggest_number_lst = [] # 값 6개 그냥 리스트에 저장

for idx in range(6):# 주사위 6면이니까 6번
    sum_numb = 0    # 리스트에 저장할 덧셈값 초기화
    first_idx = next_numb(idx) # 
    numberr = dice_lst[0][first_idx] #0번 주사위 다음 위치에 숫자
    #print(big_number(dice_lst[0][idx], numberr)) # 첫번째 주사위 양면 출력
    sum_numb += big_number(int(dice_lst[0][idx]), int(numberr))
    for dc_numb in range(1, T): # test에서 1에서 5까지
        number1 = numberr # 다음 주사위
        idx2 = dice_lst[dc_numb].index(numberr)
        numberr = dice_lst[dc_numb][next_numb(idx2)]
        number2 = numberr # 다음 주사위 반대편
        #print(number1,number2) # 다음 주사위 양면 출력
        sum_numb += big_number(int(number1), int(number2))
    biggest_number_lst.append(sum_numb)
    print(biggest_number_lst)

biggest_number_lst.sort()
print(biggest_number_lst[-1])