import sys
sys.stdin = open("4865.txt")

def maxx(lst):
    big = 0
    for i in lst:
        if i > big:
            big = i
    return big

t = int(input())

for test_case in range(1,t+1):
    a = input()
    lst = input()

    my_dic = {}  # 딕셔너리 생성
    for i in a:  # 전부 0으로 초기화
        my_dic[i] = 0
    
    for i in lst:  # 오류뜨면 그냥 넘어감
        try:
            my_dic[i] += 1
        except:
            pass
    
    print(f'#{test_case} {maxx(my_dic.values())}')