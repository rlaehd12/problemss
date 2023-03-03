import sys
sys.stdin = open('input2304.txt')

# T = int(input())
# pilar_lst = [] #리스트 하나에 저장
# for pillar in range(T):#리스트로 입력받기
#     pilar_lst.append(list(map(int, input().split())))

# pilar_lst.sort()

# #######################제일 큰거 중심으로 양쪽부터?
# middle = max(pilar_lst,key= lambda x: x[1])# 높이 젤 높은거 중앙으로 생각/ 그게 양끝이면 나중에 생각//상관 없을듯
# #print(middle)
# #print(pilar_lst.index(middle))
# max_lheight = pilar_lst[0][:] #위치, 왼쪽 높이
# max_rheight = pilar_lst[-1][:]#위치, 오른쪽 높이

# areas = 0 #넓이 초기화

# # 왼쪽 넓이 - 처음부터 큰거 만날때까지 계속 자기자신 곱합, 큰거 만나면 그 큰게 자기자신이 됨
# for left in pilar_lst[:pilar_lst.index(middle)]:
#     #print(left)
#     if max_lheight[1] < left[1]:
#         areas += (left[0] - max_lheight[0]) * max_lheight[1]#넓이는 위치 * 높이
#         max_lheight = left
#     pass
# else:
#     areas += (middle[0] - max_lheight[0]) * max_lheight[1]
# #
# # print('--middle--')

# # 오른쪽 넓이 - 위에거 반대로
# for right in pilar_lst[-1:pilar_lst.index(middle):-1]:
#     #print(right)
#     if max_rheight[1] < right[1]:
#         areas += (max_rheight[0] - right[0]) * max_rheight[1]#넓이는 위치 * 높이
#         max_rheight = right
#     pass
# else:
#     areas += (max_rheight[0] - middle[0]) * max_rheight[1]

# areas += middle[1]

# print(areas)

N = int(input())
lst = []
# x 좌표순서로 버블정렬
for _ in range(N):
    lst.append(list(map(int, input().split())))

for j in range(1, len(lst)):
    for jj in range(len(lst)-j):
        if lst[jj][0] > lst[jj+1][0]:
            lst[jj], lst[jj + 1] = lst[jj + 1], lst[jj]
# lst.sort()
h_max = [0,0]

print(lst)
for l in lst:
    if l[1] >= h_max[1]:
        h_max = l # 최고점 구하기
print(h_max)

# 최고점 인덱스 추출
cnt = 0 # 최고점 인덱스 추출
for ll in lst:
    if ll == h_max:
        break
    cnt += 1
# print(cnt)

# 최고점보다 왼쪽에 있는 점들 검사
h = lst[0][1]
g = lst[0][0]
m_hap = 0
for i in range(cnt+1):
    if lst[i][1] >= h:
        m_hap += h * (lst[i][0] - g)
        g = lst[i][0]
        h = lst[i][1]
# print(m_hap)

# 최고점보다 오른쪽에 있는 점들 검사
lst2 = lst[cnt:][::-1] # 최고점 기준 오른쪽에 있는 점들
# print(lst2)
h = lst2[0][1]
g = lst2[0][0]
for i in range(len(lst2)):
    if lst2[i][1] >= h:
        m_hap += h * ((g+1) - (lst2[i][0]+1))
        g = lst2[i][0]
        h = lst2[i][1]

m_hap += h_max[1] # 기둥 넒이 추가
print(m_hap)