import sys
sys.stdin = open("1234.txt")

for tc in range(1,4):
    n, lst = input().split()
    n = int(n)

    while True:
        for i in range(n-1):
            if lst[i] == lst[i+1]:  # 연속 두개 같으면
                n -= 2  # 문자열 길이 줄이기
                lst = lst[:i] + lst[i+2:]  # 그 두개 제외한거 반환하고 다시 검사
                break
        else:
            break
    
    print(f'#{tc} {lst}')