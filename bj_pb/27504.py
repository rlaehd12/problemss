import sys
sys.stdin = open("27504.txt")


ans = []
N = int(input())
music = []  # 음악들
for _ in range(N):
    music.append(list(map(int, input().split())))

L = int(input())  # 멜로디 길이
melody = list(map(int, input().split()))

pattern = []  # 패턴 저장
for i in range(L-1):
    pattern.append(melody[i+1] - melody[i])

for one in range(N):
    k=0
    i = 0
    cur_pattern = []
    while i < (len(music[one])-1):
        cur = music[one][i+1]-music[one][i]
        # print(i, cur)

        if cur == pattern[k]:
            k += 1
            cur_pattern.append(cur)

        elif cur != pattern[k]:  # 검사 시작
            cur_pattern.append(cur)
            # print(cur_pattern, k, one+1)
            chk = 1
            # for chk in range(1, k+1):
            while chk < k+1:
                if cur_pattern[chk] == pattern[0]:  # 앞부분이 같으면 끝까지 중복패턴 검사

                    if k-chk == 0:  # 지금이 끝부분이면 검사 종료
                        cur_pattern = cur_pattern[chk:]
                        k = 1
                        break

                    for chk_pattern in range(1, k+1 - chk):
                        if cur_pattern[chk+chk_pattern] != pattern[chk_pattern]:
                            chk += chk_pattern  # 이거 없으면 시간초과남
                            break
                    else:
                        cur_pattern = cur_pattern[chk:]
                        k = chk_pattern+1
                        break
                chk += 1
            else:
                cur_pattern = []
                k = 0

        if k == L-1:
            ans.append(one+1)
            break
        i += 1

if ans:
    for i in ans:
        print(i, end=' ')
else:
    print(-1)

