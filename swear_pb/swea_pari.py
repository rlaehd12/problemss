T = int(input())

for test_case in range(1, T + 1):
    d, a, b, f = map(int, input().split())
    time = d / (a + b)

    print(f'#{test_case} {time * f}')