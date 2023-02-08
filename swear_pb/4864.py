import sys
sys.stdin = open("4864.txt")

t = int(input())

for test_case in range(1,t+1):
    n = input()
    m = input()
    
    # if n in m:
    #     print(f'#{test_case} 1')
    # else:
    #     print(f'#{test_case} 0')


    cnt = 0  # 길이 구하기
    for i in n:
        cnt += 1
    n_len = cnt
    
    cnt = 0
    for i in m:
        cnt += 1
    m_len = cnt

    for i in range(m_len - n_len +1):  # m 길이만큼 잘라서 전부 확인
        if m[i:i+n_len] == n:
            print(f'#{test_case} 1')
            break
    else:
        print(f'#{test_case} 0')
