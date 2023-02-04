n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

lst.sort()



print(round(sum(lst)/n))  ####
print(lst[n//2])  ####
count = 1
big = 0
big_num = 0
idx = 0
if n > 2:  # 2보다 많으면
    for i in range(n-1):  # 마지막 전까지
        if lst[i] == lst[i+1]:  # 지금, 그 뒤가 같은지 확인
            count += 1  # 카운트 더하기
            if i == n-2:  # 현재 마지막이라면
                if big < count:
                    big_num = lst[i]
                elif big == count and idx != 2:
                    big_num = lst[i]
        else:  # 지금과 그 뒤가 다르면
            if big < count:  # 현재까지 쌓인 카운트가 이전보다 크면 바꿈
                big = count
                big_num = lst[i]
                idx = 1
            elif big == count and idx != 2:  # 현재 카운트가 이전과 같고 두번째 최빈값이면 바꿈
                big_num = lst[i]
                idx += 1
            count = 1  # 달라졌으니 카운트 초기화
else:
    big_num = lst[-1]

print(big_num)

print(lst[-1]-lst[0])  ####