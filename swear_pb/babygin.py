import sys
sys.stdin = open("babygin.txt")

def baby(lst):
    if lst[2] == lst[1]+1 and lst[1] == lst[0]+1:
        return True
    return False

def gin(lst):
    if lst[0] == lst[1] and lst[1] == lst[2]:
        return True
    return False

def perm(i, k):
    if ans[0] == 2:  # babygin 판명되면 더 안해도 됨
        return

    # base case
    if i == k:
        ans[0] = 0
        clst = p_lst[0:3]
        if baby(clst) or gin(clst):
            ans[0] += 1
        clst = p_lst[3:]
        if baby(clst) or gin(clst):
            ans[0] += 1

    else:
        for j in range(k):
            if visited_lst[j] == 0:  # 아직 안썼스면
                visited_lst[j] = 1
                p_lst[i] = lst[j]

                perm(i+1, k)

                visited_lst[j] = 0  # 원상복귀
                # p_lst[i] = visited_lst[j]  # 이건 어짜피 덮어씌우니까 복귀 안시켜도 됨

T = int(input())
k = 6
for tc in range(T):
    ans = [0]  # 0이면 false 1 = true
    lst = list(map(int, input()))
    p_lst = [0] * 6  # 작업할거
    visited_lst = [0] * 6  # 방문한거
    perm(0, 6)
    if ans[0] == 0:
        print(False)
    else:
        print(True)