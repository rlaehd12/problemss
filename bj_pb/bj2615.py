import sys
sys.stdin = open("input2615.txt")

baduk = []

def check(i, j, badukpan):
    for k in range(5):  # 오른쪽
        if j + k <= 18 and badukpan[i][j] == baduk[i][j+k]: continue
        else: break
    else:
        if (j-1 >= 0 and badukpan[i][j] == baduk[i][j-1]) or (j+5 <= 18 and badukpan[i][j] == baduk[i][j+5]):
            pass
        else:
            return True, 0
    for k in range(5):  # 우하향
        if i + k <= 18 and j + k <= 18 and badukpan[i][j] == baduk[i+k][j+k]: continue
        else: break
    else:
        if (i-1 >= 0 and j-1 >= 0 and badukpan[i][j] == baduk[i-1][j-1]) or (i+5 <= 18 and j+5 <= 18 and badukpan[i][j] == baduk[i+5][j+5]):
            pass
        else:
            return True, 0
    for k in range(5):  # 하향
        if i + k <= 18 and badukpan[i][j] == baduk[i+k][j]: continue
        else: break
    else:
        if (i-1 >= 0 and badukpan[i][j] == baduk[i-1][j]) or (i+5 <= 18 and badukpan[i][j] == baduk[i+5][j]):
            pass
        else:
            return True, 0
    for k in range(5):  # 좌하향
        if i+k <= 18 and j-k >= 0 and badukpan[i][j] == baduk[i+k][j-k]: continue
        else: break
    else:
        if (i-1 >= 0 and j+1 <= 18 and badukpan[i][j] == baduk[i-1][j+1]) or (i+5 <= 18 and j-5 >= 0 and badukpan[i][j] == baduk[i+5][j-5]):
            pass
        else:
            return True, 1

for _ in range(19):
    baduk.append(input().replace(' ', ''))

for i in range(19):
    #print(baduk[i])
    pass

final = []

for i in range(19):
    for j in range(19):
        if baduk[i][j] == '1' or baduk[i][j] == '2':  # 만약 1,2 찾았으면
            mycheck = check(i, j, baduk)
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
