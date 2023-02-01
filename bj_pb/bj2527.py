import sys
sys.stdin = open('input2527.txt')

def ispoint(lst):
    # # 리스트 뒤쪽 사각형이 더 위, 오른쪽에 있으면
    # if lst[2] + lst[3] < lst[6] + lst[7]:
    #     # 두 좌표 같음
    #     if ((lst[2] == lst[4]) and (lst[3] == lst[5])) or ((lst[6] == lst[0]) and (lst[5] == lst[3])):
    #         return True
    # # 앞쪽 사각형이 더 오른쪽
    # else: 
    #     # 위랑 마찬가지
    #     if ((lst[6] == lst[0]) and (lst[7] == lst[1])) or ((lst[2] == lst[4]) and (lst[1] == lst[7])):
    #         return True
    # return False
    # 4군데 점 중 하나라도 같으면 점
    if (lst[0] == lst[6] and lst[1] == lst[7]) or (lst[2] == lst[4] and lst[1] == lst[7]) or (lst[2] == lst[4] and lst[3] == lst[5]) or (lst[0] == lst[6] and lst[3] == lst[5]):
        return True
    else:
        return False
    

def isline(lst):
    # # 리스트 뒤쪽 사각형이 더 위, 오른쪽에 있으면
    # if lst[2] + lst[3] < lst[6] + lst[7]:
    #     # 두 좌표 같음
    #     if ((lst[2] == lst[4]) or (lst[3] == lst[5])) or ((lst[6] == lst[0]) or (lst[5] == lst[3])):
    #         return True
    # # 앞쪽 사각형이 더 오른쪽
    # else: 
    #     # 위랑 마찬가지
    #     if ((lst[6] == lst[0]) or (lst[7] == lst[1])) or ((lst[2] == lst[4]) or (lst[1] == lst[7])):
    #         return True
    # return False
    if (lst[0] == lst[6] and lst[1] != lst[7]) or (lst[2] != lst[4] and lst[1] == lst[7]) or (lst[2] == lst[4] and lst[3] != lst[5]) or (lst[0] != lst[6] and lst[3] == lst[5]):
        return True
    else:
        return False


def isnot(lst):
    # # 리스트 뒤쪽 사각형이 더 위, 오른쪽에 있으면
    # if lst[2] + lst[3] < lst[6] + lst[7]:
    #     # 두 좌표중 하나만 더 크면 됨
    #     if (lst[2] < lst[4]) or (lst[3] < lst[5]):
    #         return True
    # # 앞쪽 사각형이 더 오른쪽
    # else: 
    #     # 위랑 마찬가지
    #     if (lst[6] < lst[0]) or (lst[7] < lst[1]):
    #         return True
    # return False
    if (lst[6] < lst[0]) or (lst[7] < lst[1]) or (lst[2] < lst[4]) or (lst[3] < lst[5]):
        return True
    else:
        return False


# a ,b, c, d # 사각형, 선분, 점, 없음
for i in range(4):
    m_lst = list(map(int, input().split()))
    #print(m_lst)

    if ispoint(m_lst):
        print('c')
    elif isline(m_lst):
        print('b')
    elif isnot(m_lst):
        print('d')
    else:
        print('a')