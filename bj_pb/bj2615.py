import sys
sys.stdin = open("input2615.txt")

baduk = []
di = [0,1,1,1]
dj = [1,1,0,-1]

def clean_check(i, j, baduk):  # 아직 수정 덜한 코드 ## 육목 반대쪽 확인, 
    for r in range(4):
        for l in range(5):
            if 0 <= i+di[r]*l and 18 >= i+di[r]*l and 0 <= i+dj[r]*l and 18 >= i+dj[r]*l:  # 범위 안나감
                if baduk[i+di[r]*l][j+dj[r]*l] == baduk[i][j]:  # 계속 같으면
                    continue
                else:
                    break
            else:
                break
        else:  # 끝까지 같으니 육목 확인
            if 0 <= i+di[r]*5 and 18 >= i+di[r]*5 and 0 <= i+dj[r]*5 and 18 >= i+dj[r]*5:  # 범위 안나감
                if baduk[i+di[r]*5][j+dj[r]*5] == baduk[i][j]:  # 또 같으면
                    break
                else:
                    return True,0
            else:
                break
    pass


# def check(i, j, badukpan):
#     for k in range(5):  # 오른쪽
#         if j + k <= 18 and badukpan[i][j] == baduk[i][j+k]: continue
#         else: break
#     else:
#         if (j-1 >= 0 and badukpan[i][j] == baduk[i][j-1]) or (j+5 <= 18 and badukpan[i][j] == baduk[i][j+5]):
#             pass
#         else:
#             return True, 0
#     for k in range(5):  # 우하향
#         if i + k <= 18 and j + k <= 18 and badukpan[i][j] == baduk[i+k][j+k]: continue
#         else: break
#     else:
#         if (i-1 >= 0 and j-1 >= 0 and badukpan[i][j] == baduk[i-1][j-1]) or (i+5 <= 18 and j+5 <= 18 and badukpan[i][j] == baduk[i+5][j+5]):
#             pass
#         else:
#             return True, 0
#     for k in range(5):  # 하향
#         if i + k <= 18 and badukpan[i][j] == baduk[i+k][j]: continue
#         else: break
#     else:
#         if (i-1 >= 0 and badukpan[i][j] == baduk[i-1][j]) or (i+5 <= 18 and badukpan[i][j] == baduk[i+5][j]):
#             pass
#         else:
#             return True, 0
#     for k in range(5):  # 좌하향
#         if i+k <= 18 and j-k >= 0 and badukpan[i][j] == baduk[i+k][j-k]: continue
#         else: break
#     else:
#         if (i-1 >= 0 and j+1 <= 18 and badukpan[i][j] == baduk[i-1][j+1]) or (i+5 <= 18 and j-5 >= 0 and badukpan[i][j] == baduk[i+5][j-5]):
#             pass
#         else:
#             return True, 1


for _ in range(19):
    baduk.append(input().replace(' ', ''))

# for i in range(19):
#     print(baduk[i])
#     pass

final = []

for i in range(19):
    for j in range(19):
        if baduk[i][j] == '1' or baduk[i][j] == '2':  # 만약 1,2 찾았으면
            mycheck = clean_check(i, j, baduk)
            final.append(mycheck)
            if mycheck != None:
                if mycheck[1] == 0:
                    print(baduk[i][j])
                    print(i+1, j+1)
                else:
                    print(baduk[i][j])
                    print(i+5, j-3)


if final.count(None) == len(final):
    print(0)
