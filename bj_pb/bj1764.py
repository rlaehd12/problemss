# 받은 값중 겹치는거 출력

N, M = map(int, input().split()) # 몇개인지 받음
count = 0
nset = set() # 집합 초기화
mlist = []   # 리스트 초기화

for i in range(N): #N개 만큼 집합에 받음
    nset.add(input())

for j in range(M):          #M개 만큼
    word = input()          #글자 받음
    if word in nset:        #글자가 집합에 있으면
        count += 1          #한개 더함
        mlist.append(word)  #리스트에 매달음
mlist.sort()                #정렬
print(count)                #몇개인지 출력
for i in mlist:             #리스트 전부 출력
    print(i)