import sys
sys.stdin = open('input2304.txt')

T = int(input())
pilar_lst = [] #리스트 하나에 저장
for pillar in range(T):#리스트로 입력받기
    pilar_lst.append(list(map(int, input().split())))

pilar_lst.sort()

#######################제일 큰거 중심으로 양쪽부터?
middle = max(pilar_lst,key= lambda x: x[1])# 높이 젤 높은거 중앙으로 생각/ 그게 양끝이면 나중에 생각//상관 없을듯
#print(middle)
#print(pilar_lst.index(middle))
max_lheight = pilar_lst[0][:] #위치, 왼쪽 높이
max_rheight = pilar_lst[-1][:]#위치, 오른쪽 높이

areas = 0 #넓이 초기화

# 왼쪽 넓이 - 처음부터 큰거 만날때까지 계속 자기자신 곱합, 큰거 만나면 그 큰게 자기자신이 됨
for left in pilar_lst[:pilar_lst.index(middle)]:
    #print(left)
    if max_lheight[1] < left[1]:
        areas += (left[0] - max_lheight[0]) * max_lheight[1]#넓이는 위치 * 높이
        max_lheight = left
    pass
else:
    areas += (middle[0] - max_lheight[0]) * max_lheight[1]
#
# print('--middle--')

# 오른쪽 넓이 - 위에거 반대로
for right in pilar_lst[-1:pilar_lst.index(middle):-1]:
    #print(right)
    if max_rheight[1] < right[1]:
        areas += (max_rheight[0] - right[0]) * max_rheight[1]#넓이는 위치 * 높이
        max_rheight = right
    pass
else:
    areas += (max_rheight[0] - middle[0]) * max_rheight[1]

areas += middle[1]

print(areas)