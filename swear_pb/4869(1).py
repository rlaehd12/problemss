import sys
sys.stdin = open("4869.txt")

# t = int(input())
#
# for tc in range(1, t+1):
#     n = int(input())//10  # 10으로 나눈거로 받음
#     cnt = 1
#     for i in range(n//2):  # 1 2개씩 없애고 2로 바꾸면 몫만큼 나옴
#         denomi = 1
#         numer = 1
#         for j in range(1, i+2):  # 조합 구하기
#             denomi *= (n-i-j)
#             numer *= j
#         cnt += int(denomi/numer)*(2**(i+1))  # 순열에서 2 개수만큼 제곱
#     print(f'#{tc} {cnt}')

t = int(input())
for case in range(1, t + 1):
    n = int(input())
    m = int(n / 10)

    d = [0, 1, 3]
    for i in range(3, m + 1):
        d.append(d[i - 1] + 2 * d[i - 2])

    print(f'#{case}', d[m])
