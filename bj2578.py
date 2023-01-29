import sys
sys.stdin = open('input2578.txt')

bingo = []       # 2차원
new_bingo = []   # 1차원
isbing = set()
count = 0        # 몇번째인지 세기
check_lst = []   # 집합 가진 체크리스트 만들기
isend = False    # 그냥 끝내려고

#체크리스트 만들기
for i in range(5):
    check_lst.append(set(range(i,25,5)))
for i in range(5):
    check_lst.append(set(range(5 * i, 5 * i + 5)))
check_lst.append({0,6,12,18,24})
check_lst.append({4,8,12,16,20})


for i in range(5): # 빙고 받기
    a = list(map(int, input().split()))
    bingo.append(a)

for k in bingo: # 2차원 1차원으로 풀기
    new_bingo += k

# 일단 5개 그냥 받기
for j in map(int, input().split()):
    count += 1
    isbing.add(new_bingo.index(j))


# 나머지 20개 받으면서 확인
for j in map(int, input().split()):
    if isend == True: ## 종료 조건이 참이면 끝냄
        break
    count += 1
    isbing.add(new_bingo.index(j)) # 지금 들어온 값의 위치 집합에 더함
    check3 = 0
    for check in check_lst: # 체크리스트 돌면서 빙고 나왔는지 확인
        if isbing.issuperset(check):
            check3 += 1
    else:
        if check3 >= 3: # 3개 이상 빙고 만들었으니까
            print(count)# 몇번째인지 출력하고 종료조건 참으로 만듬
            isend = True

#### 그냥 위에거 복붙함
for j in map(int, input().split()):
    if isend == True:
        break
    count += 1
    isbing.add(new_bingo.index(j))
    check3 = 0
    for check in check_lst:
        if isbing.issuperset(check):
            check3 += 1
    else:
        if check3 >= 3:
            print(count)
            isend = True
for j in map(int, input().split()):
    if isend == True:
        break
    count += 1
    isbing.add(new_bingo.index(j))
    check3 = 0
    for check in check_lst:
        if isbing.issuperset(check):
            check3 += 1
    else:
        if check3 >= 3:
            print(count)
            isend = True
for j in map(int, input().split()):
    if isend == True:
        break
    count += 1
    isbing.add(new_bingo.index(j))
    check3 = 0
    for check in check_lst:
        if isbing.issuperset(check):
            check3 += 1
    else:
        if check3 >= 3:
            print(count)
            isend = True
