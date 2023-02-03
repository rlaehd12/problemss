import sys
sys.stdin = open("input1208.txt")

# def maxx_idx(lst):
#     max_v = lst[0]  # 기본은 맨 앞
#     idx = 0  # 인덱스 값 저장할거
#     count = 0  # 인덱스 값 표시할거
#     for i in lst:  # 리스트 역으로 순회하면서
#         if max_v < i:  # 큰값 만나면 값을 바꿈
#             max_v = i
#             idx = count
#         count += 1
#     return max_v, idx  # 값, 위치 반환

# def minn_idx(lst):
#     max_v = lst[0]  # 기본은 맨 앞
#     idx = 0  # 인덱스 값 저장할거
#     count = 0  # 인덱스 값 표시할거
#     for i in lst:  # 리스트 역으로 순회하면서
#         if max_v > i:  # 큰값 만나면 값을 바꿈
#             max_v = i
#             idx = count
#         count += 1
#     return max_v, idx  # 값, 위치 반환


# for tc in range(1,11):

#     dumping_numb = int(input())
#     area_lst = list(map(int, input().split()))

#     for dump in range(dumping_numb):  # 덤핑 횟수만큼
#         area_lst[maxx_idx(area_lst)[1]] -= 1  # 큰거 줄임
#         area_lst[minn_idx(area_lst)[1]] += 1  # 작은거 올림

#     #print(maxx_idx(area_lst)[0] - minn_idx(area_lst)[0])

#     print(f'#{tc} {maxx_idx(area_lst)[0] - minn_idx(area_lst)[0]}')  # 높은거 낮은거 뺌

# 1208_flatten

'''
평탄화/높은 곳의 상자를 낮은 곳에 옮긴다.최고점과 최저점의 간격을 줄인다.
max와 min의 차이가 최대 1이내가 된다
제한된 횟수만큼 옮기는 작업을 한 후 max와 min의 차이 반환
덤프 :가장 높은 곳 =>가장 낮은 곳
'''
T = 10

for tc in range(1, T + 1):
    N = int(input())  # 덤프 횟수

    box = list(map(int, input().split()))  # input받을 box 리스트
    bsort = [0] * len(box)    # 정렬될 box리스트
    bcount = [0] * (101)      # 0~100 까지 담긴다.

    n = 1
    while n <= N:

        bcount = [0] * (101)      # 0~100 까지 담긴다.
        for i in range(0, len(box)):
            bcount[box[i]] += 1

        # 2. C_2 생성, 누적합으로 조정
        for i in range(1, len(bcount)):
            bcount[i] += bcount[i - 1]

        # 3. B에 넣기
        for i in range(len(bsort) - 1, -1, -1):
            bcount[box[i]] -= 1
            bsort[bcount[box[i]]] = box[i]

        bsort[0] += 1
        bsort[-1] -= 1
        box = bsort[:]
        n += 1  # 횟수 올라가기
    
    bsort.sort()
    print(f'#{tc} {bsort[-1] - bsort[0]}')