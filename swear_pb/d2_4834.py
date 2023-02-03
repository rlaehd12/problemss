import sys
sys.stdin = open("input4834.txt")


def maxx(lst,lst_len):
    max_v = lst[-1]  # 기본은 맨 뒤
    idx = lst_len  # 인덱스 값 저장할거
    count = lst_len  # 인덱스 값 표시할거
    for i in lst[::-1]:  # 리스트 역으로 순회하면서
        if max_v < i:  # 큰값 만나면 값을 바꿈
            max_v = i
            idx = count
        count -= 1
    return max_v, idx  # 값, 인덱스 반환



t = int(input())

for tc in range(t):
    n = int(input())
    count = [0] * 10  # 카운팅 배열 생성

    cards = input()  # 그냥 문자열로 받음

    for card in cards:
        count[int(card)] += 1  # 그 인덱스 값 증가
    
    print(f'#{tc+1} {maxx(count, 10)[1]-1} {maxx(count, 10)[0]}')  # 카운팅 배열에서 큰거 찾고 인덱스 받음