import sys
sys.stdin = open("input4831.txt")

t = int(input())

for tc in range(1, t + 1):
    k, n, m = map(int, input().split())  # k칸 이동 가능  # n 종점 숫자  # m 충전기 설치 정류장 수
    station_numb_lst = list(map(int, input().split()))

    #print(station_numb_lst)
    myloc = 0
    notend = True
    charging = 0  # 배터리 충전 횟수


    while notend:  # 끝났는지 확인용
        myloc += k  # 내 위치 최대만큼 가봄
        if myloc >= n:  # 목표보다 멀리가면 끝냄
            print(f'#{tc} {charging}')
            break
        
        for i in range(k):  # 갈수 있는 최대부터 역으로 돌아오면서 확인
            if (myloc - i) in set(station_numb_lst):  # 충전소 있는 버정 집합에 내 위치가 있다면
                myloc = myloc - i
                charging += 1
                break
                pass
        else:  # for문 다 돌았는데 충전소 없으면
            print(f'#{tc} 0')
            notend = False
        pass

    

    pass